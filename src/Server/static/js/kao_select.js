(function (a) {
    'use strict';

    angular.module('kao.select', ['ui.bootstrap'])
        .directive('kaoSelect', function() {
            return {
              restrict: 'E',
              replace: true,
              scope: {
                  options: '=options',
                  current: '=current',
                  callback: '=callback'
              },
              templateUrl: 'static/partials/directives/kao_select.html'
            }});
})(angular);