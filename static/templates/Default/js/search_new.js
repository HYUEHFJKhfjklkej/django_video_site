var new_search_delay   = false;
var new_search_value   = '';

$(function() {
	$("body").on("click", "#searchsuggestions a", function(e) {
		e.preventDefault();
		var url = $(this).find("a").context.href;
		$.post(dle_root + "engine/mod_punpun/search/frontend/ajax_search.php", {news: url}, function(data) {
			
		});
		window.location.href = url;
	});
});

function NewFastSearch() {
	$('#ajax_search').attr('autocomplete', 'off');
	$('#ajax_search').blur(function(){
		$('#searchsuggestions').fadeOut();
	});

	$('#ajax_search').keyup(function() {
		var inputString = $(this).val();

		if(inputString.length == 0)
			$('#searchsuggestions').fadeOut();
		else {
			if (new_search_value != inputString && inputString.length > 1) {
				clearInterval(new_search_delay);
				new_search_delay = setInterval(function() { new_do_search(inputString); }, 200);
			}
		}
	});
};

function new_do_search(inputString) {
	clearInterval(new_search_delay);

	$('#searchsuggestions').remove();

	$("body").append("<div id='searchsuggestions' style='display:none'></div>");

	$.post(dle_root + "engine/mod_punpun/search/frontend/ajax_search.php", {query: ""+inputString+""}, function(data) {
		$('#searchsuggestions').html(data).fadeIn().css({'position' : 'absolute', top:0, left:0}).position({
			my: "left top",
			at: "left bottom",
			of: "#ajax_search",
			collision: "fit flip"
		});
	});

	new_search_value = inputString;
};
NewFastSearch();