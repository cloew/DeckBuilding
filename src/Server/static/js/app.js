'use strict';

angular.module('DeckBuilding', ['ngRoute', 'DeckBuildingControllers'])
	.config(['$routeProvider',
		function($routeProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/start_game.html',
			controller: 'StartGameController'
		})
		.when('/game/:gameId', {
			templateUrl: 'static/partials/game.html',
			controller: 'GameController'
		})
		.otherwise({
			redirectTo: '/'
		})
		;
	}])
    .directive('card', function() {
      return {
          restrict: 'E',
          replace: 'true',
          template: '<img src="static/images/vulnerability.jpg" width="124" height="174" title="{{card.name}}|{{card.cost}}"</img>'
      }})
      .directive('handCard', function() {
      return {
          restrict: 'E',
          replace: 'true',
          template: '<div><card style="cursor:pointer" ng-click="playCard($index)"></card></div>'
      }})
      .directive('lineUpCard', function() {
      return {
          restrict: 'E',
          replace: 'true',
          template: '<div style="width: 150px; float:left; position: relative;"><card style="cursor:pointer;" ng-click="buyCard($index, '+"'"+'lineUp'+"'"+')"></card></div>'
      }})
      .directive('actionCard', function() {
      return {
          restrict: 'E',
          replace: 'true',
          scope: {
              action: '=action',
              args: '=actionArguments',
              index: '=index',
              card: '=card'
          },
          template: '<div style="width: 150px; float:left; position: relative;"><card style="cursor:pointer;" ng-click="action(index, args);"></card></div>'
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
      }});