'use strict';

/* Services */
var as = angular.module('services', ['ngResource']);

as.factory('Flask', ['$resource',
  function($resource){
    return $resource("http://127.0.0.1:5000/topos/:id", {}, {
        query:  { method:'GET'},
        add:    { method:'POST' },
        update: { method:'PUT', params:{id:''}},
        delete: { method:'DELETE', params:{id:''}},
        });
  }]);
