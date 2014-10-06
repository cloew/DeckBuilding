'use strict';

var controllers = angular.module('DeckBuildingControllers', ['ui.bootstrap', 'ngCookies']);

controllers.service('notificationService', function() {
  var notifications = [];
  var setNotifications = function(newNotifications) {
      notifications = newNotifications;
  };
  var getNotifications = function(){
      return notifications;
  };
  return {
    setNotifications: setNotifications,
    getNotifications: getNotifications
  };
});

controllers.factory('NotificationFactory', function() {
    var typeToData = {"HIT_BY_ATTACK":{"forYou":"You were hit by the attack.",
                                       "forOthers":"was hit by the attack.",
                                       "type":"danger"}};
    var getMessage = function(notification) {
        if (notification.isYou) {
            return typeToData[notification.type].forYou;
        } else {
            return notification.name + " " + typeToData[notification.type].forOthers;
        }
    };
    var getType = function(notification) {
        return typeToData[notification.type].type;
    };
    return function(notification) {
        return {"message":getMessage(notification), "type":getType(notification)};
    };
});

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

controllers.controller('LobbiesController', function($scope, $cookies, $http, $location, $timeout) {
    (function tick() {
        $http.get('/api/lobbies').success(function(data) {
            $scope.lobbies = data['lobbies'];
            if (!$scope.donePolling) {
                $scope.pollPromise = $timeout(tick, 1000);
            }
        }).error(function(error) {
            console.log(error);
            if (!$scope.donePolling) {
                $scope.pollPromise = $timeout(tick, 1000);
            }
        });
    })();
    $scope.startNewLobby = function() {
        $http.post('/api/lobbies', {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.trackLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.joinLobby = function(lobbyId) {
        $http.post('/api/lobbies/'+lobbyId+'/join', {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.trackLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.trackLobby = function(data) {
        $cookies.playerId = data.playerId;
        $scope.goToLobby(data.lobbyId);
    };
    $scope.goToLobby = function(lobbyId) {
        $location.path('/lobbies/'+lobbyId);
    };
    $scope.$on('$destroy', function() {
        $scope.donePolling = true;
        $timeout.cancel($scope.pollPromise);
    });
});
controllers.controller('LobbyController', function($scope, $cookies, $http, $location, $timeout, $routeParams) {
    $scope.setLobby = function(data) {
        $scope.lobby = data;
        $scope.lobby.allPlayers = [$scope.lobby.you];
        $scope.lobby.allPlayers.push.apply($scope.lobby.allPlayers, $scope.lobby.players);
        if (data.gameId) {
            $location.path('/game/'+data.gameId);
        }
    };
    (function tick() {
        $http.get('/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId).success(function(data) {
            $scope.setLobby(data);
            if (!$scope.donePolling) {
                $scope.pollPromise = $timeout(tick, 1000);
            }
        }).error(function(error) {
            console.log(error);
            if (!$scope.donePolling) {
                $scope.pollPromise = $timeout(tick, 1000);
            }
        });
    })();
    $scope.changeCharacter = function() {
        $http.post('/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId+'/changecharacter', {'character':$scope.newCharacter}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.changeName = function() {
        $http.post('/api/lobbies/'+$routeParams.lobbyId+'/player/'+$cookies.playerId+'/changename', {'name':$scope.newName}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setLobby(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.startGame = function() {
        $http.post('/api/lobbies/'+$routeParams.lobbyId+'/start', {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $location.path('/game/'+data.gameId);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.$on('$destroy', function() {
        $scope.donePolling = true;
        $timeout.cancel($scope.pollPromise);
    });
});
controllers.controller('GameController', function($scope, $cookies, $http, $location, $routeParams, $timeout, $modal, notificationService) {
    var rootUrl = '/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId;
    $scope.setGame = function(data) {
        $scope.game = data['game'];
        notificationService.setNotifications($scope.game.notifications);
        if ($scope.game.isOver) {
            $location.path('/game/'+$scope.game.id+'/results');
        }
        if ($scope.game.request && !$scope.hasModal) {
            $scope.openRequestModal()
        }
    };
    (function tick() {
        $http.get(rootUrl).success(function(data) {
            $scope.setGame(data);
            if (!$scope.donePolling) {
                $scope.pollPromise = $timeout(tick, 1000);
            }
        }).error(function(error) {
            console.log(error);
            if (!$scope.donePolling) {
                $scope.pollPromise = $timeout(tick, 1000);
            }
        });
    })();
    $scope.actions = {};
    $scope.actions.activateCard = function(index, source) {  
        $http.post(rootUrl+'/activate', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.actions.buyCard = function(index, source) {  
        $http.post(rootUrl+'/buy', {'index':index, 'source':source}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.actions.playCard = function(index) {
        $http.post(rootUrl+'/play', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.endTurn = function(index) {
        $http.post(rootUrl+'/endturn').success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.chooseOption = function(index) {
        $http.post(rootUrl+'/choose', {'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.pickCard = function(indices) {
        $http.post(rootUrl+'/pickcard', {'indices':indices}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.defend = function(defending, index) {
        $http.post(rootUrl+'/defend', {'defending':defending, 'index':index}, {headers: {'Content-Type': 'application/json'}}).success(function(data) {
            $scope.setGame(data);
        }).error(function(error) {
            alert(error);
        });
    };
    $scope.openRequestModal = function() {
        var controllers = {'CHOICE':{'templateUrl':'static/partials/choose_option.html',
                                     'controller':'ChooseOptionController'},
                           'DEFEND':{'templateUrl':'static/partials/defend.html',
                                     'controller':'DefendController'},
                           'PICK_CARD':{'templateUrl':'static/partials/pick_card.html',
                                        'controller':'PickCardController'},
                           'PICK_UP_TO_N_CARD':{'templateUrl':'static/partials/pick_up_to_n_cards.html',
                                                'controller':'PickCardController'}};
    
        var controller = controllers[$scope.game.request.type];
        $scope.hasModal = true;
        var modalInstance = $modal.open({
          templateUrl: controller.templateUrl,
          backdrop: 'static',
          keyboard : false,
          controller: controller.controller,
          resolve: {
            parent: function () {
              return $scope;
            }},
          size: 'lg'
        });
    };
    $scope.$on('$destroy', function() {
        $scope.donePolling = true;
        $timeout.cancel($scope.pollPromise);
    });
});
controllers.controller('GameResultsController', function($scope, $cookies, $http, $routeParams, $timeout, $modal) {
    var rootUrl = '/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId+'/results';
    $http.get(rootUrl).success(function(data) {
        $scope.results = data;
    }).error(function(error) {
        console.log(error);
    });
});

controllers.controller('ChooseOptionController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    
    $scope.chooseOption = function(index) {
        $scope.parent.chooseOption(index);
        $modalInstance.dismiss('cancel');
        $scope.parent.hasModal = false;
    };
});

controllers.controller('PickCardController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    $scope.actions = {};
    $scope.indices = [];
    $scope.actions.pickCard = function(index) {
        $scope.indices.push(index);
        if ($scope.indices.length ===  $scope.request.number) {
            $scope.sendChoices();
        }
    };
    $scope.hasCard = function(index) {
        return $scope.indices.indexOf(index) > -1;
    };
    $scope.sendChoices = function() {
        $scope.parent.pickCard($scope.indices);
        $modalInstance.dismiss('cancel');
        $scope.parent.hasModal = false;
    };
});

controllers.controller('DefendController', function($scope, $modalInstance, parent) {
    $scope.parent = parent;
    $scope.request = parent.game.request;
    $scope.actions = {};
    $scope.actions.pickCard = function(index) {
        $scope.parent.defend(true, index);
        $scope.dismissModal();
    };
    $scope.abortDefense = function() {
        $scope.parent.defend(false);
        $scope.dismissModal();
    };
    $scope.dismissModal = function() {
        $modalInstance.dismiss('cancel');
        $scope.parent.hasModal = false;
    };
});

controllers.controller('NotificationController', function($scope, $timeout, notificationService, NotificationFactory) {
    (function tick() {
        var notifications = notificationService.getNotifications();
        $scope.notifications = [];
        angular.forEach(notifications, function(notification) {
            $scope.notifications.push(NotificationFactory(notification));
        });
        if (!$scope.donePolling) {
            $scope.pollPromise = $timeout(tick, 1000);
        }
    })();
    $scope.$on('$destroy', function() {
        $scope.donePolling = true;
        $timeout.cancel($scope.pollPromise);
    });
});