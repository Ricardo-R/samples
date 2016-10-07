var app = angular.module('app', ['ui.router']);

app.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
    $urlRouterProvider.otherwise('/home');

    var states = [
        {
            name: 'home',
            url: '/home',
            views:{
                '@':{
                    templateUrl: 'template/main.html',
                    controller: 'mainCtrl'
                }
            }
        },
        {
            name: 'home.bg',
            url: '/bg',
            views:{
                '@home':{
                    templateUrl: 'template/bg.html',
                    controller: 'bgCtrl'
                }
            }
        },
    ];

    for (var i in states){
        console.log('XXX', states[i])
        $stateProvider.state(states[i].name, states[i]);
    }
}]);

app.controller('mainCtrl', ['$scope', '$state', function($scope, $state){
    $scope.home = 'TEST_HOME_STR';
}]);

app.controller('bgCtrl', ['$scope', '$state', function($scope, $state){
    $scope.bg = 'TEST_BG_STR';
}]);

//angular.bootstrap(document, ['app']);
