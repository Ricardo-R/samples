(function() {
require.config = {
    baseUrl : 'app',
    paths   : {
        'ctrl'      : 'controllers',
        'subctrl'   : 'subcontrollers',
        'services'  : 'services',
    },
    shim    : {
        'ctrl'   : {
            'exports'   : 'controllers'
        },
        'subctrl': {
            'exports'   : 'subcontrollers'
        },
        'services'      : {
            'exports'   : 'services'
        },
    }
};

define(function () {
    return 'Load ctrls ok'
});
})();
