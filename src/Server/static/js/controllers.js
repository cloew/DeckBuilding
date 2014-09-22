'use strict';

var controllers = angular.module('DeckBuildingControllers', ['ui.bootstrap', 'ngCookies']);

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

controllers.controller('LobbiesController', function($scope, $cookies, $http, $location, $timeout) {
    (function tick() {
        $http.get('/api/lobbies').success(function(data) {
            $scope.lobbies = data['lobbies'];
            $scope.pollPromise = $timeout(tick, 1000);
        }).error(function(error) {
            alert(error);
            $scope.pollPromise = $timeout(tick, 1000);
        });
    })();
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
    $scope.$on('$destroy', function() {
        $timeout.cancel($scope.pollPromise);
    });
});
controllers.controller('LobbyController', function($scope, $cookies, $http, $location, $timeout, $routeParams) {
    (function tick() {
        $http.get('/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId).success(function(data) {
            $scope.lobby = data;
            $scope.pollPromise = $timeout(tick, 1000);
        }).error(function(error) {
            alert(error);
            $scope.pollPromise = $timeout(tick, 1000);
        });
    })();
    $scope.changeCharacter = function() {
        $http.post('/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId+'/changecharacter', {'character':$scope.newCharacter}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.lobby = data;
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
    $scope.$on('$destroy', function() {
        $timeout.cancel($scope.pollPromise);
    });
});
controllers.controller('GameController', function($scope, $http, $routeParams, $modal) {
    $scope.setGame = function(data) {
        $scope.game = data['game'];
        if ($scope.game.request) {
            $scope.openRequestModal()
        }
    };
    $http.get('/api/game/'+$routeParams.gameId).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    $scope.actions = {};
    $scope.actions.activateCard = function(index, source) {  
        $http.post('/api/game/'+$routeParams.gameId+'/activate', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.actions.buyCard = function(index, source) {  
        $http.post('/api/game/'+$routeParams.gameId+'/buy', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.actions.playCard = function(index) {
        $http.post('/api/game/'+$routeParams.gameId+'/play', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.endTurn = function(index) {
        $http.post('/api/game/'+$routeParams.gameId+'/endturn').success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.chooseOption = function(index) {
        $http.post('/api/game/'+$routeParams.gameId+'/choose', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.pickCard = function(index) {
        $http.post('/api/game/'+$routeParams.gameId+'/pickcard', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.openRequestModal = function() {
        var controllers = {'CHOICE':{'templateUrl':'static/partials/choose_option.html',
                                     'controller':'ChooseOptionController'},
                           'PICK_CARD':{'templateUrl':'static/partials/pick_card.html',
                                        'controller':'PickCardController'}};
    
        var controller = controllers[$scope.game.request.type];
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

controllers.controller('ChooseOptionController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    
    $scope.chooseOption = function(index) {
        $scope.parent.chooseOption(index);
        $modalInstance.dismiss('cancel');
    };
});

controllers.controller('PickCardController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    $scope.actions = {};
    $scope.actions.pickCard = function(index) {
        $scope.parent.pickCard(index);
        $modalInstance.dismiss('cancel');
    };
});