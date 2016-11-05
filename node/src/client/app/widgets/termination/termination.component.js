(function(){

	var module = angular.module('app.widgets');

	module.component('sfgTermination', {
		templateUrl:'app/widgets/termination/termination.html',
		controller: TerminationController
	});

	TerminationController.$inject = ['$sce', 'apiservice']

	function TerminationController($sce, apiservice){
		var vm = this;

		vm.createTermination = createTermination;

		//////////////


		function createTermination(){

			console.log('create termination');

			var term = {
				firstname: 'Fred',
				surname: 'Feuerstein'
			}

			apiservice.termination.save(term, 
				function(response){
				console.log('got termination', (response));

				var file = new Blob([response.data], {type: 'application/pdf'});

       			var fileURL = URL.createObjectURL(file);
       			console.log('got termination', (response), file, fileURL);

       			vm.content = $sce.trustAsResourceUrl(fileURL);
			});

		}
	}
})();