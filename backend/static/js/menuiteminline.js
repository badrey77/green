

$(document).ready(function() {
    const $ = django.jQuery;
    $.each($('div[id^=menuitems-]'), function () {
        const h3 = $(this).children("h3");
        const body = $(this).children("fieldset")
        h3.on('click', function (target) {
            body.toggleClass('collapsed')
        });
    });
});

