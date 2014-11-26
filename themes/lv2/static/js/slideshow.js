function getPreviousNode(n) {
	var p = n.previousSibling;
	while (p && p.nodeType !== 1) {
		p = p.previousSibling;
	}
	return p;
}

function startSlideShow() {
	var slideshow = document.getElementById("slideshow"),
		imgs      = slideshow.getElementsByTagName("img"),
		n         = imgs.length,
		m         = Math.floor((Math.random() * n)),
		pred      = getPreviousNode(slideshow);

	// Shrink width of predecessor so gallery fits beside it
	if (pred) {
		pred.style.width   = "50%";
		pred.style.display = "inline-block";
	}

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
