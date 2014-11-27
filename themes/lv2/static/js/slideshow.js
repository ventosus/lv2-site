function startSlideShow() {
	var slideshow = document.getElementById("slideshow"),
		imgs      = slideshow.getElementsByTagName("img"),
		n         = imgs.length,
		m         = Math.floor((Math.random() * n));

	// Start transition of initial image
	imgs[m].className = "fadein";
	m                 = (m + 1) % n;

	function tick() {
		// Fade out the previous image, and fade in the next
		var prev = (m + n - 1) % n,
			next = (m + 1) % n;

		imgs[prev].className = "";
		imgs[m].className    = "fadeout";
		imgs[next].className = "fadein";

		m = (m + 1) % n;
	}
	window.setInterval(tick, 4000);
}

startSlideShow();
