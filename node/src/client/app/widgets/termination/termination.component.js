(function(){

	var module = angular.module('app.widgets');

	module.component('sfgTermination', {
		templateUrl:'app/widgets/termination/termination.html',
		controller: TerminationController,
    bindings: {
      onCreation: '&'
    }
	});

	TerminationController.$inject = ['$sce', 'apiservice']

	function TerminationController($sce, apiservice){
		var vm = this;

		vm.createTermination = createTermination;

    vm.term = {};

    vm.term = {
      firstname: 'Fred',
      surname: 'Feuerstein',
      street: 'Steinbruch 1',
      city: '12345 Steinhausen'
    };

		//////////////


		function createTermination(){

			console.log('create termination');



			apiservice.termination.save(vm.term,
				function(response){

				var file = new Blob([response.data], {type: 'application/pdf'});

       		var fileURL = URL.createObjectURL(file);
          console.log('callback', vm.onCreation);

          var result = $sce.trustAsResourceUrl(fileURL);
          vm.onCreation({termination: result});
          //vm.term = {};
			});

		}
	}
})();
