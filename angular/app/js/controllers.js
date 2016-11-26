'use strict';

/* Controllers */

var as = angular.module('controllers', []);

as.controller('contentCtrl', ['$scope', '$rootScope', function ($scope, $rootScope ){ 
	$rootScope.breads = [{path:'home', url:'home'}];
	$rootScope.title = 'Home';
	$scope.login = function (username, pwd){
		if (username === 'admin' && pwd === '12345'){
			$scope.loginPass = 'PASS';
		}else{
			$scope.loginPass = 'FAIL';
		}
	};

	$scope.roles = [
		'guest', 
		'user', 
		'customer', 
		'admin'
	];
	$scope.user = {
		roles: ['user']
	};
	$scope.checkAll = function() {
		$scope.user.roles = angular.copy($scope.roles);
	};
	$scope.uncheckAll = function() {
		$scope.user.roles = [];
	};
	$scope.checkFirst = function() {
		$scope.user.roles.splice(0, $scope.user.roles.length); 
		$scope.user.roles.push('guest');
	}; 
}]);

as.controller('dashboardCtrl', ['$rootScope', function ($rootScope){ 
        $rootScope.breads = [
            {path:'home', url:'home' }, 
            {path:'dashboard', url:'home.dashboard'}
        ];
        $rootScope.title = 'Dashboard';
}]);

as.controller('campaigns', ['$rootScope', function ($rootScope){ 
    $rootScope.breads = [
        {path:'home', url:'home'},
        {path:'campaigns', url:'home.campaigns'}
    ];
    $rootScope.title = 'Campaigns';
}]);

as.controller('subscribers', ['$scope', '$rootScope',  
    function ($scope, $rootScope){ 
        $rootScope.breads = [
            {path:'home', url:'home'},
            {path:'subscribers', url:'home.subscribers'}
        ];
        $rootScope.title = 'Subscribers';
}]);
