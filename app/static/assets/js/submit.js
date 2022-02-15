const t = document.getElementById('form');

t.addEventListener("keyup", function(e) {
	if (e.key == "Enter") t.submit();
});