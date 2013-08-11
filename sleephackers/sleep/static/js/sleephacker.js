var sleephacker = angular.module('sleephacker', ['ui.bootstrap']) 

.controller('LoginCtrl', function($scope, $http){
	$scope.login = function () {
		$http.get('/login');
	}
})


.controller('ResultsCtrl', function($scope){
	
	$scope.analysis = {day: "today"};
	$scope.analysis.results = [
    {
      title: "drink coffee after 5PM",
      content: "Dynamic Group Body - 1",
      isFlipped: false,
      flipClass: ""
    },
    {
      title: "exercise before bed",
      content: "Dynamic Group Body - 2",
      isFlipped: false,
      flipClass: ""
    }
  	];

	$scope.enoughData = "true";
		
	$scope.flip = function (index) {
		
		console.log("FLIP");
		
		for (var i = 0; i < $scope.analysis.results.length; i++) {
			if (i != index){
				$scope.analysis.results[i].flipClass = "";
			}
		}
		
		if ($scope.analysis.results[index].flipClass == ""){
			$scope.analysis.results[index].flipClass = "flipped";
			console.log($scope.analysis.results[index].flipClass);
		} else {
			$scope.analysis.results[index].flipClass = "";
		}
	};

})


.controller('TagGroupsCtrl', function($scope){

	$scope.taggroups = [
    {
      name: "Caffeine",
      tags: [
      		{name: "Caffeine"},
      		{name: "Coffee"},
      		{name: "Tea"},
      		{name: "Chocolate"}
      		]
    },
    {
      name: "Alcohol",
      tags: [
      		{name: "Alcohol"},
      		{name: "Wine"},
      		{name: "Beer"}
      		]
    }
  	];


})

;
	
