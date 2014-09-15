'use strict';

angular.module('DeckBuildingDirectives', [])
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
              action: '=action',
              args: '=actionArguments',
              index: '=index',
              card: '=card'
          },
          template: '<div style="width: 150px; float:left; position: relative;"><card style="cursor:pointer;" ng-click="action(index, args);"><div ng-transclude></div></card></div>'
      }})
      .directive('cardList', function() {
      return {
          restrict: 'E',
          replace: 'true',
          scope: {
              cards: '=cards',
              action: '=action',
              args: '=actionArguments'
          },
          template: '<div style="display: inline-block; width: 100%;"><action-card action="action" action-arguments="args" card="card" index="$index" ng-repeat="card in cards"></action-card></div>'
      }})
      .directive('deck', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              deck: '=deck',
              action: '=action',
              args: '=actionArguments',
          },
          templateUrl: 'static/partials/directives/deck.html'
      }})
      .directive('deckCounter', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              deck: '=deck',
          },
          templateUrl: 'static/partials/directives/deck_counter.html'
      }});