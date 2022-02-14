const state = document.getElementById("btn-check");
const c = document.getElementById("collapse-menu")
const s = document.getElementById("static-menu");

state.addEventListener("change", function(e) {
	if (e.target.checked) {
		c.style.display = "flex";
	} else {
		c.style.display = "none";
	}
});

window.addEventListener("resize", function(e) {
	if (state.checked) {
		if (this.screen.width > 650) {
			state.checked = false;
			c.style.display = "none";
		}
	}
});

window.addEventListener("beforeunload", function() {
	state.checked = false;
});