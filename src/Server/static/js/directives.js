'use strict';

angular.module('DeckBuildingDirectives', ["DeckBuildingServices"])
    .directive('stretchToBottom', function($window, $document, $timeout) {
        return {
          restrict: 'A',
          replace: true,
          link: function (scope, element, attrs) {
            var originalHeight = undefined;
            var applyHeight = function() {
              var currentHeight = element.height();
              var newHeight = $window.innerHeight - element.offset().top - 10;
              if (originalHeight === undefined) {
                originalHeight = currentHeight;
              }
              if (newHeight > originalHeight) {
                element.height(newHeight);
              }
              else {
                element.height(originalHeight);
              }
            };
            angular.element($window).bind('resize', function() {
              scope.$apply(function() {
                  applyHeight();
              });
            });
            $document.ready(function() {$timeout(applyHeight, 200);});
          }
        }})
    .directive('lobbyOverview', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              lobby: '=lobby'
          },
          templateUrl: 'static/partials/directives/Lobby/lobby_overview.html'
      }})
    .directive('lobbySettings', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              lobby: '=lobby'
          },
          templateUrl: 'static/partials/directives/Lobby/lobby_settings.html'
      }})
    .directive('lobbyPlayerSettings', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              lobby: '=lobby',
              lobbyWrapper: '=lobbyWrapper'
          },
          templateUrl: 'static/partials/directives/Lobby/lobby_player_settings.html'
      }})
    .directive('lobbyPlayers', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              lobby: '=lobby'
          },
          templateUrl: 'static/partials/directives/Lobby/lobby_players.html'
      }})
    .directive('characterSelection', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          scope: {
              lobbyWrapper: '=lobbyWrapper'
          },
          controller: function($scope, $http) {
            $scope.lobbyWrapper.addCallback(function(lobby) {
                $scope.currentCharacter = lobby.you.character;
                if (!$scope.hovering && $scope.viewedCharacter !== $scope.currentCharacter) {
                    $scope.viewCurrentCharacter();
                }
            })
            $http.get('/api/characters').success(function(data) {
                $scope.characters = data.characters;
            }).error(function(error) {
                console.log(error);
            });
              
            $scope.changeCharacter = function(name) {
                $scope.lobbyWrapper.changeCharacter(name);
            };
            $scope.viewCharacter = function(character) {
                $scope.hovering = true;
                $scope.viewedCharacter = character;
            };
            $scope.viewCurrentCharacter = function() {
                $scope.viewedCharacter = $scope.currentCharacter;
                $scope.hovering = false;
            };
          },
          templateUrl: 'static/partials/directives/character_selection.html'
      }})
    .directive('cardImage', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          scope: {
              image: '=image',
              size: '=size'
          },
          templateUrl: 'static/partials/directives/card_image.html'
      }})
    .directive('card', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          templateUrl: 'static/partials/directives/card.html'
      }})
    .directive('character', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              actions: '=actions',
              character: '=character',
              thumbnail: '=thumbnail'
          },
          link: function(scope, elements, attrs) {
              scope.index = 0;
          },
          templateUrl: 'static/partials/directives/character.html'
      }})
    .directive('character-thumb', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              character: '=character'
          },
          templateUrl: 'static/partials/directives/character-thumb.html'
      }})
      .directive('actionCard', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          scope: {
              actions: '=actions',
              index: '=index',
              card: '=card',
              deck: '=deck',
              size: '=size',
              includeCardActions: '@'
          },
          compile: function(element, attrs){
            if (attrs.includeCardActions === undefined) { attrs.includeCardActions = true; }
          },
          template: '<div style="width: 150px; float:left; position: relative;"><card><div ng-transclude></div></card></div>'
      }})
      .directive('cardList', function() {
      return {
          restrict: 'E',
          replace: 'true',
          scope: {
              cards: '=cards',
              actions: '=actions',
              size: '@'
          },
          compile: function(element, attrs){
            if (attrs.size === undefined) { attrs.size = 'medium'; }
          },
          template: '<div style="display: inline-block; width: 100%;"><action-card actions="actions" size="size" card="card" index="$index" ng-repeat="card in cards" ng-hide="$scope.indices.indexOf($index) > -1"></action-card></div>'
      }})
      .directive('availableCards', function() {
      return {
          restrict: 'E',
          replace: 'true',
          templateUrl: 'static/partials/directives/available_cards.html'
      }})
      .directive('chosenCards', function() {
      return {
          restrict: 'E',
          replace: 'true',
          templateUrl: 'static/partials/directives/chosen_cards.html'
      }})
      .directive('deck', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              deck: '=deck',
              displayTopCard: '=displayTopCard',
              actions: '=actions',
              size: '=size'
          },
          templateUrl: 'static/partials/directives/deck.html'
      }})
    .directive('notification', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/Notifications/notification.html'
      }})
    .directive('cardsNotification', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/Notifications/cards_notification.html'
      }})
    .directive('revealNotification', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/Notifications/reveal_notification.html'
      }})
    .directive('standardNotification', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/Notifications/standard_notification.html'
      }})
    .directive('cardLinks', function() {
      return {
          restrict: 'E',
          replace: false,
          templateUrl: 'static/partials/directives/Notifications/card_links.html'
      }})
      .directive('cardIcons', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          templateUrl: 'static/partials/directives/CardIcons/card_icons.html'
      }})
      .directive('actionCardIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/CardIcons/action_card_icon.html'
      }})
      .directive('activateIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/CardIcons/activate_icon.html'
      }})
      .directive('buyIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/CardIcons/buy_icon.html'
      }})
      .directive('examineCardIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/CardIcons/examine_card_icon.html'
      }})
      .directive('examineCharacterIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/CardIcons/examine_character_icon.html'
      }})
      .directive('examineDeckIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/CardIcons/examine_deck_icon.html'
      }})
      .directive('pickIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/CardIcons/pick_icon.html'
      }})
      .directive('playIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/CardIcons/play_icon.html'
      }})
      .directive('deckCounter', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              count: '=count',
          },
          templateUrl: 'static/partials/directives/CardIcons/deck_counter.html'
      }})
    .directive('player', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {player: '=',
                  actions: '=',
                  isYou: '@'},
          compile: function(element, attrs){
            if (attrs.isYou === undefined) { attrs.isYou = false; }
          },
          controller: function($scope, requestModalService) {
            $scope.requestService = requestModalService;
          },
          templateUrl: 'static/partials/directives/player.html'
      }})
    .directive('hand', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/hand.html'
      }})
    .directive('lineUp', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/line_up.html'
      }})
    .directive('notifications', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/notifications.html'
      }})
    .directive('ongoing', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/ongoing.html'
      }})
    .directive('played', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/played.html'
      }})
    .directive('turn', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/turn.html'
      }})
    .directive('picker', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              name: '@',
              options: '=',
              current: '=',
              callback: '='
          },
          controller: function($scope) {
            $scope.previous = function(current) {
                current -= 1;
                $scope.callback(current);
            };
            $scope.next = function(current) {
                current += 1;
                $scope.callback(current);
            };
          },
          templateUrl: 'static/partials/directives/picker.html'
      }})
    .directive('deckPicker', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              name: '@',
              role: '@',
              deck: '='
          },
          controller: function($scope, lobbyService) {
            $scope.changeDeck = function(current) {
                lobbyService.findLobbyWrapper().changeDeck($scope.role, current);
            };
          },
          templateUrl: 'static/partials/directives/deck_picker.html'
      }})
    .directive('villainCountPicker', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              name: '@',
              villainCountInfo: '='
          },
          controller: function($scope, lobbyService) {
            $scope.changeCount = function(current) {
                lobbyService.findLobbyWrapper().changeVillainCount(current);
            };
          },
          templateUrl: 'static/partials/directives/villain_count_picker.html'
      }})
    .directive('cardGroup', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {header: '@',
                  cards: '=',
                  actions: '='},
          templateUrl: 'static/partials/directives/card_group.html'
      }})
    .directive('headerDiv', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          scope: {header: '@'},
          templateUrl: 'static/partials/directives/header_div.html'
      }})
    .directive('playerResults', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/player_results.html'
      }});