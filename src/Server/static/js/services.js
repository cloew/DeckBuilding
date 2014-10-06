'use strict';

var services = angular.module('DeckBuildingServices', []);

services.service('notificationService', function() {
  var notifications = [];
  var setNotifications = function(newNotifications) {
      notifications = newNotifications;
  };
  var getNotifications = function(){
      return notifications;
  };
  return {
    setNotifications: setNotifications,
    getNotifications: getNotifications
  };
});

services.factory('StandardNotificationFactory', function() {
    var typeToData = {"DEFENDED":{"forYou":"You defended with ",
                                  "forOthers":"defended with",
                                  "alertType":"success"},
                      "HIT_BY_ATTACK":{"forYou":"You were hit by the attack.",
                                       "forOthers":"was hit by the attack.",
                                       "alertType":"danger"}};
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
        return {"message":getMessage(notification), "alertType":getAlertType(notification)};
    }};
});

services.factory('CardsNotificationFactory', function(StandardNotificationFactory) {
    return {"type":"CARDS", "load": function(notification) {
        var result = StandardNotificationFactory.load(notification);
        result.cards = notification.cards;
        return result;
    }};
});

services.factory('NotificationFactory', function(StandardNotificationFactory, CardsNotificationFactory) {
    var typeToData = {"HIT_BY_ATTACK":StandardNotificationFactory,
                      "DEFENDED":CardsNotificationFactory};
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
                parentScope.pollPromise = $timeout(tick, 30000);
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