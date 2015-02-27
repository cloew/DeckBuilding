(function(a) {
    "use strict";
    a.module('Notifications', ['Zone'])
        .service('notificationService', function() {
            var notifications = [];
            var setNotifications = function(newNotifications) {
                mergeNotifications(newNotifications);
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
        })
        .factory('notificationDisplayTypes', function() {
            return {"HIT_BY_ATTACK":"STANDARD",
                    "END_TURN":"STANDARD",
                    "START_TURN":"STANDARD",
                    "ATTACKED":"CARDS",
                    "DEFENDED":"CARDS",
                    "MOVED_CARD":"MOVEMENT",
                    "BOUGHT_CARD":"MOVEMENT",
                    "REVEAL":"REVEAL"};
        })
        .factory('notificationMessages', function() {
            var typeToData = {"HIT_BY_ATTACK":{"forYou":"You were hit by the attack.",
                                               "forOthers":" was hit by the attack."},
                              "START_TURN":{"forYou":"Your turn",
                                            "forOthers":"'s turn"},
                              "END_TURN":{"forYou":"Your turn is over",
                                          "forOthers":"'s turn is over"}};
            return {getMessage: function(notification) {
                if (notification.isYou) {
                    return typeToData[notification.type].forYou;
                } else {
                    return notification.player.name + typeToData[notification.type].forOthers;
                }}};
        })
        .directive('notifications', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/notifications.html'
            };
        })
        .directive('notification', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                    notification: '='
                },
                controller: function($scope, notificationDisplayTypes) {
                    $scope.displayType = notificationDisplayTypes[$scope.notification.type];
                },
                templateUrl: 'static/partials/directives/Notifications/notification.html'
            };
        })
        .directive('standardNotification', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                    notification: '='
                },
                controller: function($scope, notificationMessages) {
                    $scope.message = notificationMessages.getMessage($scope.notification);
                },
                templateUrl: 'static/partials/directives/Notifications/standard_notification.html'
            };
        })
        .directive('cardsNotification', function() {
            return {
                restrict: 'E',
                replace: true,
                transclude: true,
                scope: {
                    notification: '='
                },
                controller: function($scope) {
                    $scope.canSeeCards = $scope.notification.isYou || !$scope.notification.private;
                    if (!$scope.canSeeCards) {
                        for (var i = 0; i < $scope.notification.count; i++) {
                            $scope.notification.cards.push(undefined);
                        }
                    }
                },
                templateUrl: 'static/partials/directives/Notifications/cards_notification.html'
            };
        })
        .directive('movementNotification', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                    notification: '='
                },
                templateUrl: 'static/partials/directives/Notifications/movement_notification.html'
            }
        })
        .directive('revealNotification', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                    notification: '='
                },
                templateUrl: 'static/partials/directives/Notifications/reveal_notification.html'
            }
        });
})(angular);