$( document ).ready(function() {
console.log( "ready!" );
    $( "#searchclick" ).click(function() {
		$('div:not(:contains("' + search + '"))').show();
		  var search = $('#search').val();
		$('div:not(:contains("' + search + '"))').hide();
	});
});