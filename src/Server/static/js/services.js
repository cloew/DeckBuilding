'use strict';

var services = angular.module('DeckBuildingServices', ['ui.bootstrap']);

services.service('gameService', function($cookies, $http, $location, $routeParams, notificationService, requestModalService, UrlPoller) {
    var rootUrl = '/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId;
    var game = undefined;
    var startPolling = function(parentScope, callback) {
        UrlPoller(parentScope, rootUrl, function(data) {
                setGame(data);
                callback(game);
            });
    };
    var getGame = function() {
        return game;
    };
    var setGame = function(data, parentScope) {
        var oldRequest = undefined;
        if (game && game.request) {
            oldRequest = game.request;
        }
        
        game = data['game'];
        notificationService.setNotifications(game.notifications);
        if (game.isOver) {
            $location.path('/game/'+game.id+'/results');
        }
        if ((!game.request || (oldRequest && oldRequest.id != game.request.id)) && requestModalService.getModal()) {
            console.log(!game.request);
            console.log((oldRequest && oldRequest.id != game.request.id));
            console.log(oldRequest.id);
            console.log(game.request.id);
            requestModalService.closeModal();
        }
        if (game.request && !requestModalService.hasModal()) {
            requestModalService.openRequestModal(game.request);
        }
    };
    var actions = {};
    actions.activateCard = function(index, source) {  
        $http.post(rootUrl+'/activate', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    actions.buyCard = function(index, source) {  
        $http.post(rootUrl+'/buy', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    actions.playCard = function(index) {
        $http.post(rootUrl+'/play', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var endTurn = function(index) {
        $http.post(rootUrl+'/endturn').success(function(data) {
            setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var chooseOption = function(index) {
        $http.post(rootUrl+'/choose', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var pickCard = function(indices) {
        $http.post(rootUrl+'/pickcard', {'indices':indices}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var defend = function(defending, index) {
        $http.post(rootUrl+'/defend', {'defending':defending, 'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    return {
        getGame: getGame,
        startPolling: startPolling,
        actions: actions,
        endTurn: endTurn,
        chooseOption: chooseOption,
        pickCard: pickCard,
        defend: defend
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
        $http.post(rootUrl, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            trackLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var joinLobby = function(lobbyId) {
        $http.post(rootUrl+'/'+lobbyId+'/join', {headers: {'Content-Type': 'application/json'}}).success(function(data) {
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
    var rootUrl = '/api/lobbies/';
    var lobby = undefined;
    var startPolling = function(parentScope, callback) {
        UrlPoller(parentScope, '/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId, function(data) {
            setLobby(data);
            callback(lobby);
        });
    };
    var getLobby = function() {
        return lobby;
    };
    var setLobby = function(data) {
        lobby = data;
        lobby.allPlayers = [lobby.you];
        lobby.allPlayers.push.apply(lobby.allPlayers, lobby.players);
        if (data.gameId) {
            $location.path('/game/'+data.gameId);
        }
    };
    var changeCharacter = function(newCharacter) {
        $http.post(rootUrl+$routeParams.lobbyId+'/player/'+$cookies.playerId+'/changecharacter', {'character':newCharacter}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var changeName = function(newName) {
        $http.post(rootUrl+$routeParams.lobbyId+'/player/'+$cookies.playerId+'/changename', {'name':newName}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    var startGame = function() {
        $http.post(rootUrl+$routeParams.lobbyId+'/start', {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $location.path('/game/'+data.gameId);
        }).error(function(error) {
            alert(error);
        });
    };
    return {
        getLobby: getLobby,
        startPolling: startPolling,
        changeCharacter: changeCharacter,
        changeName: changeName,
        startGame: startGame
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
    var modalIsOpen = false;
    var openRequestModal = function(request) {
        var controllers = {'CHOICE':{'templateUrl':'static/partials/choose_option.html',
                                     'controller':'ChooseOptionController'},
                           'DEFEND':{'templateUrl':'static/partials/defend.html',
                                     'controller':'DefendController'},
                           'PICK_CARD':{'templateUrl':'static/partials/pick_card.html',
                                        'controller':'PickCardController'},
                           'PICK_UP_TO_N_CARD':{'templateUrl':'static/partials/pick_up_to_n_cards.html',
                                                'controller':'PickCardController'}};
    
        var controller = controllers[request.type];
        modalIsOpen = true;
        modal = $modal.open({
          templateUrl: controller.templateUrl,
          backdrop: 'static',
          keyboard : false,
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
    return {
        getModal: getModal,
        hasModal: hasModal,
        openRequestModal: openRequestModal,
        closeModal: closeModal
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
    var getMessage = function(notification) {
        if (notification.isYou) {
            return typeToData[notification.sourceType].forYou;
        } else {
            return notification.name + " " + typeToData[notification.sourceType].forOthers;
        }
    }
    return {"type":"REVEAL", "load": function(notification) {
        var result = CardsNotificationFactory.load(notification);
        result.sourceText = " from " + getMessage(notification);
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