'use strict';

var controllers = angular.module('DeckBuildingControllers', ['ui.bootstrap']);

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

controllers.controller('GameController', function($scope, $http, $routeParams, $modal) {
    $http.get('/api/game/'+$routeParams.gameId).success(function(data) {
            $scope.game = data['game'];
        }).error(function(error) {
            alert(error);
        });
    $scope.buyCard = function(index, source) {  
        $http.post('/api/game/'+$routeParams.gameId+'/buy', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.game = data['game'];
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.playCard = function(index) {
        $http.post('/api/game/'+$routeParams.gameId+'/play', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.game = data['game'];
            if ($scope.game.request) {
                $scope.openModal()
            }
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.endTurn = function(index) {
        $http.post('/api/game/'+$routeParams.gameId+'/endturn').success(function(data) {
            $scope.game = data['game'];
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.chooseOption = function(index) {
        $http.post('/api/game/'+$routeParams.gameId+'/choose', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.game = data['game'];
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.openModal = function() {
        var modalInstance = $modal.open({
          templateUrl: 'static/partials/choose_option.html',
          backdrop: 'static',
          keyboard : false,
          controller: 'ChooseOptionController',
          resolve: {
            parent: function () {
              return $scope;
            }},
          size: 'lg'
        });
    };
});

controllers.controller('ChooseOptionController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    
    $scope.chooseOption = function(index) {
        $scope.parent.chooseOption(index);
        $modalInstance.dismiss('cancel');
    };
});