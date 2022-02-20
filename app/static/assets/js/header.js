$(function() {
	$('#btn-check').change(function(e) {
		if (e.target.checked) {
			$('#collapse-menu').css('display', 'flex');
		} else {
			$('#collapse-menu').css('display', 'none');
		}
	});

	$(window).resize(function(e) {
		if ($(window).width() > 650) {
			$('#btn-check').prop('checked', false);
			$('#collapse-menu').css('display', 'none');
		}
	});

	if ($('#btn-check').is(':checked')) {
		$('#collapse-menu').css('display', 'flex');
	}
});