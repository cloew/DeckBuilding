'use strict';

var controllers = angular.module('DeckBuildingControllers', ['ui.bootstrap', 'ngCookies', 'DeckBuildingServices']);

controllers.controller('StartGameController', function ($scope, $http, $location) {
    $scope.startGame = function() {
        $http.post('/api/startgame').success(function(data) {
            $scope.game = data['game'];
            $location.path('/game/'+$scope.game.id);
        }).error(function(error) {
            alert(error);
        });
    };
});

controllers.controller('LobbiesController', function($scope, $cookies, $http, $location, UrlPoller) {
    UrlPoller($scope, '/api/lobbies', function(data) {
            $scope.lobbies = data['lobbies'];
        });
    $scope.startNewLobby = function() {
        $http.post('/api/lobbies', {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.trackLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.joinLobby = function(lobbyId) {
        $http.post('/api/lobbies/'+lobbyId+'/join', {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.trackLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.trackLobby = function(data) {
        $cookies.playerId = data.playerId;
        $scope.goToLobby(data.lobbyId);
    };
    $scope.goToLobby = function(lobbyId) {
        $location.path('/lobbies/'+lobbyId);
    };
});
controllers.controller('LobbyController', function($scope, $cookies, $http, $location, $routeParams, UrlPoller) {
    UrlPoller($scope, '/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId, function(data) {
        $scope.setLobby(data);
        });
    $scope.setLobby = function(data) {
        $scope.lobby = data;
        $scope.lobby.allPlayers = [$scope.lobby.you];
        $scope.lobby.allPlayers.push.apply($scope.lobby.allPlayers, $scope.lobby.players);
        if (data.gameId) {
            $location.path('/game/'+data.gameId);
        }
    };
    $scope.changeCharacter = function() {
        $http.post('/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId+'/changecharacter', {'character':$scope.newCharacter}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.changeName = function() {
        $http.post('/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId+'/changename', {'name':$scope.newName}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.startGame = function() {
        $http.post('/api/lobbies/'+$routeParams.lobbyId+'/start', {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $location.path('/game/'+data.gameId);
        }).error(function(error) {
            alert(error);
        });
    };
});
controllers.controller('GameController', function($scope, $cookies, $http, $location, $routeParams, $modal, notificationService, UrlPoller) {
    var rootUrl = '/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId;
    UrlPoller($scope, rootUrl, function(data) {
            $scope.setGame(data);
        });
    $scope.setGame = function(data) {
        $scope.game = data['game'];
        notificationService.setNotifications($scope.game.notifications);
        if ($scope.game.isOver) {
            $location.path('/game/'+$scope.game.id+'/results');
        }
        if ($scope.game.request && !$scope.hasModal) {
            $scope.openRequestModal()
        }
    };
    $scope.actions = {};
    $scope.actions.activateCard = function(index, source) {  
        $http.post(rootUrl+'/activate', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.actions.buyCard = function(index, source) {  
        $http.post(rootUrl+'/buy', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.actions.playCard = function(index) {
        $http.post(rootUrl+'/play', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.endTurn = function(index) {
        $http.post(rootUrl+'/endturn').success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.chooseOption = function(index) {
        $http.post(rootUrl+'/choose', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.pickCard = function(indices) {
        $http.post(rootUrl+'/pickcard', {'indices':indices}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.defend = function(defending, index) {
        $http.post(rootUrl+'/defend', {'defending':defending, 'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.openRequestModal = function() {
        var controllers = {'CHOICE':{'templateUrl':'static/partials/choose_option.html',
                                     'controller':'ChooseOptionController'},
                           'DEFEND':{'templateUrl':'static/partials/defend.html',
                                     'controller':'DefendController'},
                           'PICK_CARD':{'templateUrl':'static/partials/pick_card.html',
                                        'controller':'PickCardController'},
                           'PICK_UP_TO_N_CARD':{'templateUrl':'static/partials/pick_up_to_n_cards.html',
                                                'controller':'PickCardController'}};
    
        var controller = controllers[$scope.game.request.type];
        $scope.hasModal = true;
        var modalInstance = $modal.open({
          templateUrl: controller.templateUrl,
          backdrop: 'static',
          keyboard : false,
          controller: controller.controller,
          resolve: {
            parent: function () {
              return $scope;
            }},
          size: 'lg'
        });
    };
});
controllers.controller('GameResultsController', function($scope, $cookies, $http, $routeParams) {
    var rootUrl = '/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId+'/results';
    $http.get(rootUrl).success(function(data) {
        $scope.results = data;
    }).error(function(error) {
        console.log(error);
    });
});

controllers.controller('ChooseOptionController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    
    $scope.chooseOption = function(index) {
        $scope.parent.chooseOption(index);
        $modalInstance.dismiss('cancel');
        $scope.parent.hasModal = false;
    };
});

controllers.controller('PickCardController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    $scope.actions = {};
    $scope.indices = [];
    $scope.actions.pickCard = function(index) {
        $scope.indices.push(index);
        if ($scope.indices.length ===  $scope.request.number) {
            $scope.sendChoices();
        }
    };
    $scope.hasCard = function(index) {
        return $scope.indices.indexOf(index) > -1;
    };
    $scope.sendChoices = function() {
        $scope.parent.pickCard($scope.indices);
        $modalInstance.dismiss('cancel');
        $scope.parent.hasModal = false;
    };
});

controllers.controller('DefendController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    $scope.actions = {};
    $scope.actions.pickCard = function(index) {
        $scope.parent.defend(true, index);
        $scope.dismissModal();
    };
    $scope.abortDefense = function() {
        $scope.parent.defend(false);
        $scope.dismissModal();
    };
    $scope.dismissModal = function() {
        $modalInstance.dismiss('cancel');
        $scope.parent.hasModal = false;
    };
});

controllers.controller('NotificationController', function($scope, notificationService, NotificationFactory, Poller) {
    $scope.notifications = [];
    Poller($scope, function() {
        $scope.notifications = notificationService.getNotifications();
    });
});