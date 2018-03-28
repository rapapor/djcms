$(document).scroll(function () {
	var p = $( "#page-cont" );
	var position = p.position();
    var y = $(this).scrollTop();
    if (y > position.top) {
        $('#navbarStyle').css('background-color','#393938');
    } else {
        $('#navbarStyle').css('background-color','transparent');
    }

});