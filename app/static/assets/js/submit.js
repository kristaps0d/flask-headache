$(function() {
	$('#form-control').on('keyup', function(e) {
		if (e.which == 13) {
			console.log(e.target.value);

			target_url = '/session/reserve/' + e.target.value;

			$.ajax({
				'url': target_url,
				'type': 'GET',
				'success': function(t) {
					// console.log(t);
					location.href = "/session/" + e.target.value;
				},
				'error': function(t) {
					// console.log(t);
				}
			});
		}
	});
}); 