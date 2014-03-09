
$(function() {
    $("#id_komenco").pickmeup({
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
    
    $("#id_fino").pickmeup({
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
});
