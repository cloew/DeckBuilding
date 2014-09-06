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
          template: '<span>{{card.name}}|{{card.cost}}</span>'
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
          template: '<div><card style="cursor:pointer" ng-click="buyCard($index, '+"'"+'lineUp'+"'"+')"></card></div>'
      }});