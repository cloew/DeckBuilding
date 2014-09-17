'use strict';

angular.module('DeckBuildingDirectives', [])
    .directive('cardImage', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          scope: {
              image: '=image',
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
      .directive('actionCard', function() {
      return {
          restrict: 'E',
          replace: true,
          transclude: true,
          scope: {
              actions: '=actions',
              index: '=index',
              card: '=card'
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
          template: '<div style="display: inline-block; width: 100%;"><action-card actions="actions" card="card" index="$index" ng-repeat="card in cards"></action-card></div>'
      }})
      .directive('deck', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              deck: '=deck',
              actions: '=actions',
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
      }});