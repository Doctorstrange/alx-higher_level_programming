$(document).ready(function () {
	$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function (value) {
		$("DIV#hello").text(value.hello);
	});
});