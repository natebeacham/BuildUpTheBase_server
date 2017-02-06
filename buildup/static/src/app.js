$(function() {
	$('nav a').each(function() {
		if ($(this).attr('href') == location.pathname) {
			$(this).addClass('active');
		}
	});
})