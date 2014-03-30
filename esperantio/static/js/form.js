
$(function() {
    $("[id$='komenco']").pickmeup({
        format: 'Y-m-d',
        hide_on_select: true,
        before_show: function () {
            var $this = $(this);
            $this.pickmeup('set_date', $this.val());
        },
        change: function (formatted) {
            $(this).val(formatted);
        }
    });
    
    $("[id$='fino']").pickmeup({
        format: 'Y-m-d',
        hide_on_select: true,
        before_show: function () {
            var $this = $(this);
            $this.pickmeup('set_date', $this.val());
        },
        change: function (formatted) {
            $(this).val(formatted);
        }
    });

    $("#pickmeup-range").pickmeup({
        date: [$("[id$='komenco']").val(), $("[id$='fino']").val()],
        format: 'Y-m-d',
        flat: 'true',
        mode: 'range',
        change: function(formatted_date) {
            $("[id$='komenco']").val(formatted_date[0]);
            $("[id$='fino']").val(formatted_date[1]);
        }
    });

});
