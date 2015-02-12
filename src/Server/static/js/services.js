'use strict';

var services = angular.module('DeckBuildingServices', ['ui.bootstrap']);

services.factory('gameService', function($cookies, $http, $location, $routeParams, notificationService, requestModalService, UrlPoller) {
    function Game(rootUrl) {
        this.rootUrl = rootUrl;
        this.game = undefined;
    };
    
    Game.prototype.startPolling = function(parentScope, callback) {
        var self = this;
        UrlPoller(parentScope, this.rootUrl, function(data) {
                self.setGame(data);
                callback(self.game);
            });
    };
    Game.prototype.getGame = function() {
        return this.game;
    };
    Game.prototype.setGame = function(data, parentScope) {
        var oldRequest = undefined;
        if (this.game && this.game.turn.request) {
            oldRequest = this.game.turn.request;
        }
        
        this.game = data['game'];
        notificationService.setNotifications(this.game.notifications);
        if (this.game.isOver) {
            $location.path('/game/'+this.game.id+'/results');
        }
        if ((!this.game.turn.request || (oldRequest && oldRequest.id != this.game.turn.request.id)) && requestModalService.getModal()) {
            requestModalService.closeModal();
        }
        if (this.game.turn.request && this.game.turn.request.forYou && !requestModalService.hasModal()) {
            requestModalService.openRequestModal(this.game.turn.request);
        }
    };
    Game.prototype.activateCard = function(apiUrl, zone) {
        var self = this;
        $http.post(apiUrl, {'zone':zone}).success(function(data) {
            self.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Game.prototype.buyCard = function(apiUrl, zone) {
        var self = this;
        $http.post(apiUrl, {'zone':zone}).success(function(data) {
            self.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Game.prototype.playCard = function(apiUrl) {
        var self = this;
        $http.post(apiUrl).success(function(data) {
            self.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Game.prototype.endTurn = function() {
        var self = this;
        $http.post(this.rootUrl+'/endturn').success(function(data) {
            self.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Game.prototype.chooseOption = function(index) {
        var self = this;
        $http.post(this.rootUrl+'/choose', {'index':index}).success(function(data) {
            self.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Game.prototype.pickCard = function(indices) {
        var self = this;
        $http.post(this.rootUrl+'/pickcard', {'indices':indices}).success(function(data) {
            self.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Game.prototype.defend = function(defending, index) {
        var self = this;
        $http.post(this.rootUrl+'/defend', {'defending':defending, 'index':index}).success(function(data) {
            self.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    
    var games = {};
    return {
        findGameWrapper: function () {
            if (games[$routeParams.gameId] === undefined) {
                games[$routeParams.gameId] = new Game('/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId);
            }
            return games[$routeParams.gameId];
        }
    };
});

services.service('lobbiesService', function($cookies, $http, $location, UrlPoller) {
    var rootUrl = '/api/lobbies';
    var lobbies = undefined;
    var startPolling = function(parentScope, callback) {
        UrlPoller(parentScope, rootUrl, function(data) {
                lobbies = data['lobbies'];
                callback(lobbies);
            });
    };
    var getLobbies = function() {
        return lobbies;
    };
    var startNewLobby = function() {
        $http.post(rootUrl).success(function(data) {
            trackLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var joinLobby = function(lobby) {
        $http.post(lobby.joinUrl).success(function(data) {
            trackLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var trackLobby = function(data) {
        $cookies.playerId = data.playerId;
        goToLobby(data.lobbyId);
    };
    var goToLobby = function(lobbyId) {
        $location.path('/lobbies/'+lobbyId);
    };
    return {
        getLobbies: getLobbies,
        startPolling: startPolling,
        startNewLobby: startNewLobby,
        joinLobby: joinLobby,
        trackLobby: trackLobby,
        goToLobby: goToLobby
    };
});

services.service('lobbyService', function($cookies, $http, $location, $routeParams, UrlPoller) {
    function Lobby(rootUrl) {
        this.rootUrl = rootUrl;
        this.playerUrl = rootUrl+'/player/'+$cookies.playerId;
        this.lobby = undefined;
        this.callbacks = [];
    };
    Lobby.prototype.startPolling = function(parentScope, callback) {
        var self = this;
        self.callbacks = [callback];
        UrlPoller(parentScope, this.playerUrl, function(data) {
            self.setLobby(data);
            for (var i = 0; i < self.callbacks.length; i++) {
                self.callbacks[i](self.lobby);
            }
        });
    };
    Lobby.prototype.getLobby = function() {
        return self.lobby;
    };
    Lobby.prototype.setLobby = function(data) {
        this.lobby = data;
        this.lobby.allPlayers = [this.lobby.you];
        this.lobby.allPlayers.push.apply(this.lobby.allPlayers, this.lobby.players);
        if (data.gameId) {
            $location.path('/game/'+data.gameId);
        }
    };
    Lobby.prototype.addCallback = function(callback) {
        this.callbacks.push(callback);
    };
    Lobby.prototype.changeCharacter = function(newCharacter) {
        var self = this;
        $http.post(this.lobby.changeCharacterUrl, {'character':newCharacter}).success(function(data) {
            self.setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Lobby.prototype.changeDeck = function(role, index) {
        var self = this;
        $http.post(this.lobby.changeDeckUrl, {'role':role, 'index':index}).success(function(data) {
            self.setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Lobby.prototype.changeVillainCount = function(index) {
        var self = this;
        $http.post(this.lobby.changeNumberOfVillainsUrl, {'index':index}).success(function(data) {
            self.setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Lobby.prototype.changeName = function(newName) {
        var self = this;
        $http.post(this.lobby.changeNameUrl, {'name':newName}).success(function(data) {
            self.setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    Lobby.prototype.startGame = function() {
        $http.post(this.lobby.startGameUrl).success(function(data) {
            $location.path('/game/'+data.gameId);
        }).error(function(error) {
            alert(error);
        });
    };
    
    var lobbies = {};
    return {
        findLobbyWrapper: function () {
            if (lobbies[$routeParams.lobbyId] === undefined) {
                lobbies[$routeParams.lobbyId] = new Lobby('/api/lobbies/'+$routeParams.lobbyId);
            }
            return lobbies[$routeParams.lobbyId];
        }
    };
});

services.service('examineCardModalService', function($modal) {
    var modal = undefined;
    var modalIsOpen = false;
    var open = function(card) {
        modalIsOpen = true;
        modal = $modal.open({
          templateUrl: 'static/partials/examine_card.html',
          controller: 'ExamineCardController',
          size: 'lg',
          resolve: {
            card: function () {
              return card;
            }
          }});
    };
    var close = function(data) {
        modalIsOpen = false;
        modal.dismiss('cancel');
        modal = undefined;
    };
    return {
        open: open,
        close: close
    };
});

services.service('examineDeckModalService', function($modal) {
    var modal = undefined;
    var modalIsOpen = false;
    var open = function(deck) {
        modalIsOpen = true;
        modal = $modal.open({
          templateUrl: 'static/partials/examine_deck.html',
          controller: 'ExamineDeckController',
          size: 'lg',
          resolve: {
            deck: function () {
              return deck;
            }
          }});
    };
    var close = function(data) {
        modalIsOpen = false;
        modal.dismiss('cancel');
        modal = undefined;
    };
    return {
        open: open,
        close: close
    };
});

services.service('requestModalService', function($modal) {
    var modal = undefined;
    var currentRequest = undefined;
    var modalIsOpen = false;
    var openRequestModal = function(request) {
        currentRequest = request;
        openModal();
    };
    var openModal = function() {
        var controllers = {'CHOICE':{'templateUrl':'static/partials/choose_option.html',
                                     'controller':'ChooseOptionController'},
                           'DEFEND':{'templateUrl':'static/partials/defend.html',
                                     'controller':'DefendController'},
                           'PICK_CARD':{'templateUrl':'static/partials/pick_card.html',
                                        'controller':'PickCardController'},
                           'PICK_UP_TO_N_CARD':{'templateUrl':'static/partials/pick_up_to_n_cards.html',
                                                'controller':'PickCardController'},
                           'PICK_UP_TO_N_COST':{'templateUrl':'static/partials/pick_up_to_n_cost.html',
                                                'controller':'PickNCostController'}};
    
        var controller = controllers[currentRequest.type];
        modalIsOpen = true;
        modal = $modal.open({
          templateUrl: controller.templateUrl,
          controller: controller.controller,
          size: 'lg'
        });
    };
    var closeModal = function(data) {
        modalIsOpen = false;
        modal.dismiss('cancel');
        modal = undefined;
    };
    var getModal = function() {
        return modal;
    };
    var hasModal = function() {
        return modalIsOpen;
    };
    var getCurrentRequest = function() {
        return currentRequest;
    };
    return {
        getModal: getModal,
        hasModal: hasModal,
        openRequestModal: openRequestModal,
        openModal: openModal,
        closeModal: closeModal,
        getCurrentRequest: getCurrentRequest
    };
});

services.service('notificationService', function(NotificationFactory) {
    var notifications = [];
    var setNotifications = function(newNotifications) {
        var newWrappedNotifications = [];
        angular.forEach(newNotifications, function(notification) {
            newWrappedNotifications.push(NotificationFactory(notification));
        });
        mergeNotifications(newWrappedNotifications);
    };
    var getNotifications = function(){
        return notifications;
    };
    var mergeNotifications = function(newNotifications){
        var allIDs =[];
        angular.forEach(notifications, function(notification) {    
            allIDs.push(notification.id);
        });
        angular.forEach(newNotifications, function(notification, key) {    
            if (allIDs.indexOf(notification.id) === -1) {
                notifications.push(notification);
            }
        });
        notifications.sort(function(a, b) {
            return ((a.id < b.id) ? -1 : (a.id > b.id) ? 1 : 0)*-1;
        });
        while (notifications.length > newNotifications.length) {
            notifications.pop();
        };
    };
    return {
        getNotifications: getNotifications,
        setNotifications: setNotifications
    };
});

services.factory('StandardNotificationFactory', function() {
    var typeToData = {"DEFENDED":{"forYou":"You defended with ",
                                  "forOthers":"defended with",
                                  "alertType":"success"},
                      "HIT_BY_ATTACK":{"forYou":"You were hit by the attack.",
                                       "forOthers":"was hit by the attack.",
                                       "alertType":"danger"},
                      "REVEAL":{"forYou":"You revealed ",
                                "forOthers":"revealed "}};
    var getMessage = function(notification) {
        if (notification.isYou) {
            return typeToData[notification.type].forYou;
        } else {
            return notification.name + " " + typeToData[notification.type].forOthers;
        }
    };
    var getAlertType = function(notification) {
        return typeToData[notification.type].alertType;
    };
    return {"type":"STANDARD", "load": function(notification) {
        return {"message":getMessage(notification), "alertType":getAlertType(notification), "id":notification.id};
    }};
});

services.factory('CardsNotificationFactory', function(StandardNotificationFactory) {
    return {"type":"CARDS", "load": function(notification) {
        var result = StandardNotificationFactory.load(notification);
        result.cards = notification.cards;
        return result;
    }};
});

services.factory('RevealNotificationFactory', function(CardsNotificationFactory) {
    var typeToData = {"DECK":{"forYou":"the top of your deck.",
                              "forOthers":"the top of their deck."},
                      "HAND":{"forYou":"your hand.",
                              "forOthers":"their hand."},
                      "MAIN_DECK":{"forYou":"the top of the main deck.",
                                   "forOthers":"the top of the main deck."},};
    var getMessageWithoutPlayerName = function(notification) {
        if (notification.isYou) {
            return typeToData[notification.zoneType].forYou;
        } else {
            return typeToData[notification.zoneType].forOthers;
        }
    }
    return {"type":"REVEAL", "load": function(notification) {
        var result = CardsNotificationFactory.load(notification);
        result.zoneText = " from " + getMessageWithoutPlayerName(notification);
        return result;
    }};
});

services.factory('NotificationFactory', function(StandardNotificationFactory, CardsNotificationFactory, RevealNotificationFactory) {
    var typeToData = {"HIT_BY_ATTACK":StandardNotificationFactory,
                      "DEFENDED":CardsNotificationFactory,
                      "REVEAL":RevealNotificationFactory};
    return function(notification) {
        var factory = typeToData[notification.type]
        var newNotification = factory.load(notification);
        newNotification.type = factory.type;
        return newNotification;
    };
});

services.factory('Poller', function($timeout) {
    return function(parentScope, pollMethod) {
        (function tick() {
            pollMethod();
            if (!parentScope.donePolling) {
                parentScope.pollPromise = $timeout(tick, 1000);
            }
        })();
        parentScope.$on('$destroy', function() {
            parentScope.donePolling = true;
            $timeout.cancel(parentScope.pollPromise);
        });
    };
});

services.factory('UrlPoller', function($http, Poller) {
    return function(parentScope, url, successMethod) {
        Poller(parentScope, function() {
            $http.get(url).success(function(data) {
                successMethod(data);
            }).error(function(error) {
                console.log(error);
            });
        });
    };
});