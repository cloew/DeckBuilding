'use strict';

angular.module('DeckBuildingDirectives', [])
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
              size: '=size'
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
          },
          template: '<div style="display: inline-block; width: 100%;"><action-card actions="actions" size="\'medium\'" card="card" index="$index" ng-repeat="card in cards" ng-hide="$scope.indices.indexOf($index) > -1"></action-card></div>'
      }})
      .directive('deck', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              deck: '=deck',
              actions: '=actions',
              size: '=size'
          },
          templateUrl: 'static/partials/directives/deck.html'
      }})
      .directive('cardIcons', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          templateUrl: 'static/partials/directives/card_icons.html'
      }})
      .directive('actionCardIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/action_card_icon.html'
      }})
      .directive('activateIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/activate_icon.html'
      }})
      .directive('buyIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/buy_icon.html'
      }})
      .directive('pickIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/pick_icon.html'
      }})
      .directive('playIcon', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/play_icon.html'
      }})
      .directive('deckCounter', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              count: '=count',
          },
          templateUrl: 'static/partials/directives/deck_counter.html'
      }})
    .directive('opponent', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/opponent.html'
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
    .directive('player', function() {
      return {
          restrict: 'E',
          replace: true,
          templateUrl: 'static/partials/directives/player.html'
      }});