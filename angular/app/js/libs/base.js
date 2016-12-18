
var LIB = '/js/libs/js'
require.config = {
    paths   : {
        'jquery'    : LIB+'/jquery',
        'angular'   : LIB+'/angular',
        'uiRouter' : LIB+'/angular-ui-router',
        'Resource'  : LIB+'/angular-resource',
        'checklistModel'   : LIB+'/checklist-model'
    },
    shim    : {
        'jquery'    : {
            'exports'   : '$'
        }, 
        'angular'   : {
            'deps'      : ['jquery'],
            'exports'   : 'angular'
        },
        'uiRouter' : {
            'deps'      : ['angular'],
            'exports'   : 'ui.router'
        },
        'Resource'  : {
            'deps'      : ['angular'],
            'exports'   : '$resource'
        },
        'checklistModel': {
            'deps'      : ['angular'],
            'exports'   : 'checklistModel'
        }
    },
}

define(['$', 'angular', 'ui.router', '$resource', '$resource', 'checklistModel'],
    function() {
        return 'Load base libs ok'
});

