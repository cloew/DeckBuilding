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
controllers.controller('GameController', function($scope, gameService) {
    gameService.startPolling($scope, function(game) {
        $scope.game = game;
    });
    $scope.actions = gameService.actions;
    $scope.endTurn = gameService.endTurn;
    $scope.chooseOption = gameService.chooseOption;
    $scope.pickCard = gameService.pickCard;
    $scope.defend = gameService.defend;
});
controllers.controller('GameResultsController', function($scope, $cookies, $http, $routeParams) {
    var rootUrl = '/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId+'/results';
    $http.get(rootUrl).success(function(data) {
        $scope.results = data;
    }).error(function(error) {
        console.log(error);
    });
});

controllers.controller('ChooseOptionController', function($scope, requestModalService, gameService) {
    $scope.request = gameService.getGame().request;
    
    $scope.chooseOption = function(index) {
        gameService.chooseOption(index);
        requestModalService.closeModal();
    };
});

controllers.controller('PickCardController', function($scope, requestModalService, gameService) {
    $scope.request = gameService.getGame().request;
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
        gameService.pickCard($scope.indices);
        requestModalService.closeModal();
    };
});

controllers.controller('DefendController', function($scope, requestModalService, gameService) {
    $scope.request = gameService.getGame().request;
    $scope.actions = {};
    $scope.actions.pickCard = function(index) {
        gameService.defend(true, index);
        requestModalService.closeModal();
    };
    $scope.abortDefense = function() {
        gameService.defend(false);
        requestModalService.closeModal();
    };
});

controllers.controller('NotificationController', function($scope, notificationService, NotificationFactory, Poller) {
    $scope.notifications = [];
    Poller($scope, function() {
        $scope.notifications = notificationService.getNotifications();
    });
});