'use strict';

angular.module('DeckBuildingDirectives', ["DeckBuildingServices"])
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
                lobbyService.changeDeck($scope.role, current);
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
                lobbyService.changeVillainCount(current);
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
      }});