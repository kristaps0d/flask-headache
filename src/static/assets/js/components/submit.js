$(function() {
    $('form').each(function() {
        $(this).getElementById("room").keypress(function(e) {

            if(e.which == 10 || e.which == 13) {
                this.form.submit();
            }
        });

        $(this).find('input[type=submit]').hide();
    });
});