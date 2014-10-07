'use strict';

var services = angular.module('DeckBuildingServices', []);

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
                              "forOthers":"their hand."}};
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