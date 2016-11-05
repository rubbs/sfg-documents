(function() {
  'use strict';

  angular
    .module('app.core')
    .factory('apiservice', apiservice);

  apiservice.$inject = ['$resource', 'exception', 'logger'];
  /* @ngInject */
  function apiservice($resource, exception, logger) {

    var apiLocation = 'http://localhost:8080';

    var service = {
      termination1: $resource(apiLocation + '/api/document/termination'),
      termination: $resource(apiLocation + '/api/document/termination', {}, {
        save: {method: 'POST', transformResponse: function(data, headersGetter) { 
          return { data : data }}
          , responseType: 'arraybuffer'}
      })

    };

    return service;

  }
})();
