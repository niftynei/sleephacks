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
      title: "drink coffee before bed",
      doOrDoNot: "DON'T",
      isFlipped: false,
      flipClass: "",
      correlationStrength: "strong",
      correlationType: "negative",
      explanation: "people who drink coffee after 5pm wake up an average of 2 more times each night.",
      exampleTry: "taking your last cup of coffee before 5pm, although the earlier the better.",
      icon: "coffee.png"
    },
    {
      title: "exercise in the morning",
      doOrDoNot: "DO",
      isFlipped: false,
      flipClass: "",
      correlationStrength: "moderate",
      correlationType: "positive",
      explanation: "When you exercise vigorously, you tend to have longer deep sleep cycles throughout the night.",
      exampleTry: "spend at least 30 minutes each morning doing vigorous exercise, such as running or swimming.",
      icon: "swim.png"
    },
    {
     title: "nap during the day",
      doOrDoNot: "DON'T",
      isFlipped: false,
      flipClass: "",
      correlationStrength: "moderate",
      correlationType: "positive",
      explanation: "people who nap during the day tend to get less light and heavy sleep.",
      exampleTry: "going to bed earlier or waking up later to get a better energy boost for the coming day.",
      icon: "sleep.png"
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
	
	parseResults = function () {
		switch(title)
		{
		case "caffeine":
			break;
			
		case "alcohol":
		
			break;
			
		default:
		
		}
		
	}
	

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
	
