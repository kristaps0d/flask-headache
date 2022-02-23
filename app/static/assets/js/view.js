$(function() {
	$('.data').on('click', function() {
		$('.clipboard').text('Nokopēts!')
		navigator.clipboard.writeText($('.data').text());
		$('.clipboard').addClass('visible');
		
		setTimeout(function() {
			$('.clipboard').removeClass('visible');
		}, 900);
	});
});