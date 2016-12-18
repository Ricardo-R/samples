'use strict';

/* Controllers */

var as = angular.module('controllers', []);

as.controller('contentCtrl', ['$scope', '$rootScope', 'ModalService', '$element', '$document',
function ($scope, $rootScope, ModalService, $element, $document){ 
    console.log('$document:', $document);
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

	$scope.showComplex = function() {
		ModalService.showModal({
			templateUrl: "/templates/modal/modal-service.html",
			controller: "ComplexController",
			inputs: {
			    title: "A More Complex Example"
			}
		}).then(function(modal) {
			modal.element.modal();
			modal.close.then(function(result) {
				$scope.complexResult  = "Name: " + result.name + ", age: " + result.age;
			});
		});
	};

}]);
as.controller('ComplexController', ['$scope', '$element', 'title',
function ($scope, $element, title){ 
	$scope.name = null;
	$scope.age = null;
	$scope.title = title;
	//  This close function doesn't need to use jQuery or bootstrap, because
	//  the button has the 'data-dismiss' attribute.
	$scope.close = function() {
		close({
			name: $scope.name,
			age: $scope.age
		}, 500); // close, but give 500ms for bootstrap to animate
	};

	//  This cancel function must use the bootstrap, 'modal' function because
	//  the doesn't have the 'data-dismiss' attribute.
	$scope.cancel = function() {
		//  Manually hide the modal.
		$element.modal('hide');
		//  Now call close, returning control to the caller.
		close({
			name: $scope.name,
			age: $scope.age
		}, 500); // close, but give 500ms for bootstrap to animate
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
