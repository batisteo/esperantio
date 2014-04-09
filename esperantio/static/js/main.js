$(function() {
    $(".uzanto").click(function(e) {
        $("#uzanto-menuo").toggle();
        e.preventDefault();
        e.stopPropagation(); // for click outside
    });
    $("#lingvo").click(function(e) {
        $("#lingvo-menuo").toggle();
        e.preventDefault();
        e.stopPropagation(); // for click outside
    });
    // Close menu if clicked outside opener
    $(document).click(function(){
        $(".dinamika-menuo").hide();
    });
});
