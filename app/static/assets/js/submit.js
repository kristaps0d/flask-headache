$(function() {
	// On page load event
	$('#form-control').on('keyup', function(e) {
		if (e.which == 13) {
			target_url = '/session/reserve/' + e.target.value;

			$('.icon').text('refresh');
			$('.form-control').addClass('disabled');

			$.ajax({
				'url': target_url,
				'type': 'GET',
				'success': function(t) {
					url = "/session/" + e.target.value;
					setTimeout(function() {
						$(location).attr('href', url);
					}, 10);

					$('.icon').text('search');
					$('.form-control').removeClass('disabled');
				},
				'error': function(t) {
					$('.message').addClass("visible");
					setTimeout(function() {
						$('.message').removeClass("visible");
					}, 1500);
					
					$('.icon').text('search');
					$('.form-control').removeClass('disabled');
				}
			});
		}
	});
}); 