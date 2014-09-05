'use strict';

var controllers = angular.module('WordGuessControllers', []);

controllers.controller('StartGameController', function ($scope, $http, $location) {
    $scope.startGame = function() {
        $http.post('/api/startgame').success(function(data) {
            $scope.game = data['game'];
            $location.path('/game/'+$scope.game.id);
        }).error(function(error) {
            alert(error);
        });
    };
});

controllers.controller('GameController', function($scope, $http, $routeParams) {
    $scope.currentGuess = {'guesses':[]};
    $scope.setGame = function(game) {
        $scope.game = game;
        $scope.game.guesses = $scope.game.guesses.reverse();
        $scope.canGuess = !$scope.game.roundComplete;
    };
    $http.get('/api/'+$routeParams.gameId).success(function(data) {
            $scope.setGame(data['game']);
        }).error(function(error) {
            alert(error);
        });
    $scope.setGuess = function(guessString) {
        $scope.currentGuess.guesses = guessString.split('');
    };
    
    $scope.guess = function() {
        $http.put('/api/'+$scope.game.id+'/guess', $scope.currentGuess, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data['game']);
        }).error(function(error) {
            alert(error);
        });
    };
    
    $scope.nextRound = function() {
        $http.put('/api/'+$scope.game.id+'/nextround', $scope.currentGuess, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data['game']);
        }).error(function(error) {
            alert(error);
        });
    };
});