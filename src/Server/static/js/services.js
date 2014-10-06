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

services.factory('NotificationFactory', function() {
    var typeToData = {"HIT_BY_ATTACK":{"forYou":"You were hit by the attack.",
                                       "forOthers":"was hit by the attack.",
                                       "alertType":"danger",
                                       "type":"STANDARD"}};
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
    var getType = function(notification) {
        return typeToData[notification.type].type;
    };
    return function(notification) {
        return {"message":getMessage(notification), "alertType":getAlertType(notification), "type":getType(notification)};
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