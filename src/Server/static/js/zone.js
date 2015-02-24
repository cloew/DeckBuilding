(function(a) {
    "use strict";
    a.module('Zone', [])
        .factory('zoneNameService', function() {
            var getPlayerHeader = function(zone) {
                if (zone.isYou) {
                    return "Your";
                } else {
                    return zone.playerName + "'s";
                }
            };
            var zoneToName = {"CHARACTER":function(zone) {return "Character"},
                              "DECK":function(zone) {return getPlayerHeader(zone) + " " + "Deck"},
                              "BOTTOM_OF_DECK":function(zone) {return "Bottom of " + getPlayerHeader(zone) + " " + "Deck"},
                              "DESTROYED":function(zone) {return "Destroyed"},
                              "DISCARD_PILE":function(zone) {return getPlayerHeader(zone) + " " + "Discard Pile"},
                              "HAND":function(zone) {return getPlayerHeader(zone) + " " + "Hand"},
                              "KICK":function(zone) {return "Kick"},
                              "LINE_UP":function(zone) {return "Line-up"},
                              "MAIN_DECK":function(zone) {return "Main Deck"},
                              "BOTTOM_OF_MAIN_DECK":function(zone) {return "Bottom of the Main Deck"},
                              "ONGOING":function(zone) {return "Ongoing"},
                              "PLAYED":function(zone) {return "Played"},
                              "SUPERVILLAIN":function(zone) {return "Super Villain"},
                              "UNDER_CHARACTER":function(zone) {return "Under " + getPlayerHeader(zone) + " " + "Character"},
                              "WEAKNESS":function(zone) {return "Weakness"},}
            return {getName: function(zone) {
                    var nameRetriever = zoneToName[zone.zoneType];
                    return (nameRetriever && nameRetriever(zone)) || 'Unknown';
                }
            }
        })
        .directive('zoneName', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                  zone: '=zone'
                },
                controller: function($scope, zoneNameService) {
                    $scope.name = zoneNameService.getName($scope.zone);
                },
                templateUrl: 'static/partials/directives/Zone/zone_name.html'
            };
        });
})(angular);