'use strict';

angular.module('DeckBuilding', ['ngRoute', 'DeckBuildingControllers', 'DeckBuildingDirectives'])
	.config(['$routeProvider',
		function($routeProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/start_game.html',
			controller: 'StartGameController'
		})
		.when('/lobbies', {
			templateUrl: 'static/partials/Lobby/lobbies.html',
			controller: 'LobbiesController'
		})
		.when('/lobbies/:lobbyId', {
			templateUrl: 'static/partials/Lobby/lobby.html',
			controller: 'LobbyController'
		})
		.when('/game/:gameId', {
			templateUrl: 'static/partials/game.html',
			controller: 'GameController'
		})
		.otherwise({
			redirectTo: '/'
		})
		;
	}]);