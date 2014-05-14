
$(function() {
    komenco = $("[id$='komenco']").val();
    fino = $("[id$='fino']").val();
    
    if (komenco == '')   date = new Date();
    else if (fino == '') date = komenco;
    else                 date = [komenco, fino]
    
    $("#pickmeup-range").pickmeup({
        date: date,
        format: 'Y-m-d',
        flat: 'true',
        mode: 'range',
        change: function(formatted_date) {
            $("[id$='komenco']").val(formatted_date[0]);
            $("[id$='fino']").val(formatted_date[1]);
        }
    });

    if (komenco == '') $(".pmu-selected").removeClass("pmu-selected");

    $("#form-adreso2").hide();
    $("#aldonu-adreson").click(function (e){
        $("#form-adreso2").slideDown();
        $(this).hide();
        e.preventDefault();
    });
});
