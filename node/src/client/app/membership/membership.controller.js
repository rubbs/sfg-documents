/**
 * Created by ruben on 31.10.16.
 */
(function() {
  'use strict';

  angular
    .module('app.membership')
    .controller('MembershipController', MembershipController);

  MembershipController.$inject = ['apiservice', 'logger'];
  /* @ngInject */
  function MembershipController(dataservice, logger) {
    var vm = this;

    vm.onTermination = onTermination;

    activate();

    ////////////////////

    function activate() {
      logger.info('test');
    }

    function onTermination(termination){
      logger.info('new termination', termination);
      vm.result = termination;
    }

  }
})();
