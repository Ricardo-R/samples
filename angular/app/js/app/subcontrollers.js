'use strict';

/* Controllers */

var as = angular.module('subcontrollers', []);

as.controller('queryAll', ['$scope', '$rootScope', 'Flask',
    function ($scope, $rootScope,  Flask){ 

        $scope.projects = Flask.query(); 

        $rootScope.breads = [
            {path:'home', url:'home'},
            {path:'subscribers', url:'home.subscribers'},
            {path:'list', url:'home.subscribers.queryAll'},
        ];

}]);

as.controller('create', ['$scope', '$rootScope', '$state','Flask',
     function ($scope, $rootScope, $state, Flask){ 

        $rootScope.breads = [
            {path:'home', url:'home'},
            {path:'subscribers', url:'home.subscribers'},
            {path:'create', url:'home.subscribers.create'},
        ];

        $scope.form = function (pj, tc, fs){
            $rootScope.state = Flask.add({},{'project':pj, 'topic':tc, 'filters':fs}, function(){}, function(){}); 
            
            $rootScope.breads = [
                {path:'home', url:'home'},
                {path:'subscribers', url:'home.subscribers'},
                {path:'result', url:'home.subscribers.result'},
            ];
            $state.go('home.subscribers.result');
        };

}]);


as.controller('update', ['$scope', '$stateParams', '$rootScope', 
    '$state', 'Flask', function ($scope, $stateParams, $rootScope, $state,  Flask){ 

        $rootScope.breads = [
            {path:'home', url:'home'},
            {path:'subscribers', url:'home.subscribers'},
            {path:'update', url:'home.subscribers.update({id:"'+$stateParams.id+'"})'},
            {path:$stateParams.id, url:'home.subscribers.update({id:"'+$stateParams.id+'"})'},
        ];

        $scope.update = function(tc, fs){
            $rootScope.state = Flask.update({id:$stateParams.id}, {'topic':tc, 'filters':fs}, function(){}, function(){}); 
            $rootScope.breads = [
                {path:'home', url:'home'},
                {path:'subscribers', url:'home.subscribers'},
                {path:'result', url:'home.subscribers.result'},
            ];
            $state.go('home.subscribers.result');
            
        };
        

}]);

as.controller('delete', ['$scope', '$stateParams', '$rootScope', 'Flask','$state',
    function ($scope, $stateParams, $rootScope, Flask, $state){ 
        
        $rootScope.breads = [
            {path:'home', url:'home'},
            {path:'subscribers', url:'home.subscribers'},
            {path:'delete', url:'home.subscribers'},
            {path:$stateParams.id, url:'home.subscribers'},
        ];
        $rootScope.state = Flask.delete({id:$stateParams.id}); 
        
        $rootScope.breads = [
            {path:'home', url:'home'},
            {path:'subscribers', url:'home.subscribers'},
            {path:'result', url:'home.subscribers.result'},
        ];
        $state.go('home.subscribers.result');

}]);
