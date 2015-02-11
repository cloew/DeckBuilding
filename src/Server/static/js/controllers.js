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

controllers.controller('LobbiesController', function($scope, lobbiesService) {
    lobbiesService.startPolling($scope, function(lobbies) {
        $scope.lobbies = lobbies;
    });
    $scope.startNewLobby = lobbiesService.startNewLobby;
    $scope.joinLobby = lobbiesService.joinLobby;
    $scope.trackLobby = lobbiesService.trackLobby;
    $scope.goToLobby = lobbiesService.goToLobby;
});
controllers.controller('LobbyController', function($scope, lobbyService) {
    $scope.lobbyWrapper = lobbyService.findLobbyWrapper();
    $scope.lobbyWrapper.startPolling($scope, function(lobby) {
        $scope.lobby = lobby;
    });
    $scope.changeCharacter = function() {
        $scope.lobbyWrapper.changeCharacter($scope.newCharacter);
    };
    $scope.changeName = function() {
        $scope.lobbyWrapper.changeName($scope.newName);
    };
});
controllers.controller('GameController', function($scope, gameService) {
    var gameWrapper = gameService.findGameWrapper();
    gameWrapper.startPolling($scope, function(game) {
        $scope.game = game;
        $scope.playersPendingActions = $scope.getPlayersPendingActions();
    });
    $scope.actions = gameWrapper;
    $scope.getPlayersPendingActions = function() {
        var pending = false;
        for (var i = 0; i < $scope.game.players.length; i++) {
            pending = ($scope.game.players[i].pending !== null);
            if (pending) {break;}
        }
        return pending;
    };
});
controllers.controller('GameResultsController', function($scope, $cookies, $http, $routeParams) {
    var rootUrl = '/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId+'/results';
    $http.get(rootUrl).success(function(data) {
        $scope.results = data;
        console.log($scope.results);
    }).error(function(error) {
        console.log(error);
    });
});

controllers.controller('ChooseOptionController', function($scope, requestModalService, gameService) {
    var gameWrapper = gameService.findGameWrapper();
    $scope.request = requestModalService.getCurrentRequest();
    
    $scope.chooseOption = function(index) {
        gameWrapper.chooseOption(index);
        requestModalService.closeModal();
    };
});

controllers.controller('PickCardController', function($scope, requestModalService, gameService) {
    var gameWrapper = gameService.findGameWrapper();
    $scope.request = requestModalService.getCurrentRequest();
    $scope.actions = {};
    $scope.indices = [];
    $scope.actions.pickCard = function(index) {
        $scope.indices.push(index);
        if ($scope.indices.length ===  $scope.request.number) {
            $scope.sendChoices();
        }
    };
    $scope.hasNotChosenCard = function(index) {
        return $scope.indices.indexOf(index) === -1;
    };
    $scope.isNotAvailable = function(index) {
        return $scope.indices.indexOf(index) > -1;
    };
    $scope.sendChoices = function() {
        gameWrapper.pickCard($scope.indices);
        requestModalService.closeModal();
    };
});

controllers.controller('PickNCostController', function($scope, requestModalService, gameService) {
    var gameWrapper = gameService.findGameWrapper();
    $scope.request = requestModalService.getCurrentRequest();
    $scope.actions = {};
    $scope.indices = [];
    $scope.tooCostlyIndices = [];
    $scope.remainingCost = $scope.request.cost;
    $scope.actions.pickCard = function(index) {
        $scope.indices.push(index);
        $scope.remainingCost -= $scope.request.cards[index].cost;
        $scope.trackUnavailableIndices();
        if ($scope.shouldSend()) {
            $scope.sendChoices();
        }
    };
    $scope.trackUnavailableIndices = function() {
        for (var i = 0; i < $scope.request.cards.length; i++) {
            if ($scope.request.cards[i].cost > $scope.remainingCost) {
                $scope.tooCostlyIndices.push(i);
            }
        }
    };
    $scope.shouldSend = function() {
        for (var i = 0; i < $scope.request.cards.length; i++) {
            if (!$scope.isNotAvailable(i)) {
                return false;
            }
        }
        return true;
    }
    $scope.hasChosenCard = function(index) {
        return $scope.indices.indexOf(index) > -1;
    };
    $scope.isNotAvailable = function(index) {
        return $scope.hasChosenCard(index) || $scope.tooCostlyIndices.indexOf(index) > -1;
    };
    $scope.sendChoices = function() {
        gameWrapper.pickCard($scope.indices);
        requestModalService.closeModal();
    };
});

controllers.controller('DefendController', function($scope, requestModalService, gameService) {
    var gameWrapper = gameService.findGameWrapper();
    $scope.request = requestModalService.getCurrentRequest();
    $scope.actions = {};
    $scope.actions.pickCard = function(index) {
        gameWrapper.defend(true, index);
        requestModalService.closeModal();
    };
    $scope.abortDefense = function() {
        gameWrapper.defend(false);
        requestModalService.closeModal();
    };
});

controllers.controller('NotificationController', function($scope, notificationService, Poller) {
    $scope.notifications = [];
    Poller($scope, function() {
        $scope.notifications = notificationService.getNotifications();
    });
});

controllers.controller('ExamineCardIconController', function($scope, examineCardModalService) {
    $scope.examineCard = function(card) {
        examineCardModalService.open(card);
    };
});

controllers.controller('ExamineCharacterIconController', function($scope, examineCardModalService) {
    $scope.examineCharacter = function(character) {
        examineCardModalService.open(character);
    };
});

controllers.controller('ExamineCardController', function($scope, examineCardModalService, card) {
    $scope.card = card;
    $scope.close = function() {
        examineCardModalService.close();
    };
});

controllers.controller('ExamineDeckIconController', function($scope, examineDeckModalService) {
    $scope.examineDeck = function(deck) {
        examineDeckModalService.open(deck);
    };
});

controllers.controller('ExamineDeckController', function($scope, examineDeckModalService, deck) {
    $scope.deck = deck;
    $scope.close = function() {
        examineDeckModalService.close();
    };
});