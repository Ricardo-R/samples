var app = angular.module('app', ['ui.router', 'ipCookie']);

app.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
    $urlRouterProvider.otherwise('/bg');

    var states = [
        {
            name: 'home',
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
        {
            name: 'home.vote',
            url: '/vote',
            views:{
                '@home':{
                    templateUrl: 'template/vote.html',
                    controller: 'voteCtrl'
                }
            }
        },
    ];

    for (var i in states){
        $stateProvider.state(states[i].name, states[i]);
    }
}]);

app.controller('mainCtrl', 
['$rootScope', '$scope', 'ipCookie', '$state', '$window', '$http',
  function($rootScope, $scope, ipCookie, $state, $window, $http){
    var login = !!ipCookie('AUTH_USER');
    if (!login){
        $window.location.href = '/login';
    }
    $rootScope.userName = ipCookie('AUTH_USER');
    $scope.navs = [
        {'state':'home.bg', 'title':'BG'},
        {'state':'home.vote', 'title':'Vote'},
    ];
    var config = {}
    config.url = '/proxy/gdcauth/users?name='+$rootScope.userName;
    config.method = 'GET';
    return $http(config).success(function(data){
        console.log('auth', data); 
        try {
            $rootScope.fullname = data.items[0].fullname;
        } catch (err) {
            $rootScope.fullname = $rootScope.userName;
        }
    }).error(function(data){
        console.log('auth', data); 
    });
}]);

app.controller('bgCtrl',
['$rootScope', '$scope', '$state', '$http',
  function($rootScope, $scope, $state, $http){

    $scope.order = '';
    $scope.data = {"items":[]};
    var config = {};
    config.method = 'GET';
    config.headers = {"Content-Type":"application/json;charset=UTF-8"};
    config.url = '/proxy/sys/bg/';
    config.data = {"items":[], "trigger":"off"};

    var rps = function(config){
        console.log('config:', config);
        $http(config)
            .success(function(data){
                $scope.data = data;
                console.log('return data:', data);
            })
            .error(function(data){
                $scope.data = data;
            })
    };

    var tmp = {"id":"", "order":""};
    $scope.post = function(){
        config.data.trigger = 'off';
        config.method = 'POST';
        tmp.id = $rootScope.userName;
        tmp.fullname = $rootScope.fullname;
        tmp.order = $scope.order;
        config.data.items[0] = tmp;
        rps(config);
    };
    $scope.clear = function(){
        config.data.trigger = 'on';
        config.method = 'POST';
        rps(config);
    };
    rps(config);
}]);

app.controller('voteCtrl',
['$scope', '$state',
  function($scope, $state){
    $scope.bg = [1,2,3,4];
    $scope.lens = $scope.bg.length
}]);
//angular.bootstrap(document, ['app']);
