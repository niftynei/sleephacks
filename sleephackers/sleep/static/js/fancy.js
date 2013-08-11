$(document).ready(function(){

	$('.card').on("click", function(){
		$(this).toggleClass('flipped');
		console.log('clicked');
	});
	
	$('.flashcard').on("click", function(){
		$(this).toggleClass('flipped');
		console.log('clicked');
	});
	
	

});