$(function() {
    $(".atendilo").hide();
    
    $(".menua-sxaltilo").click(function(e) {
        var menu_id = $(this).attr('target');
        $(menu_id).toggle();
        e.preventDefault();
        e.stopPropagation(); // for click outside
    });
    // Close menu if clicked outside opener
    $(document).click(function(e) {
        $(".dinamika-menuo").hide();
    });

    $("a.malaktiva").click(function(e) {
        e.preventDefault();
    });
});
