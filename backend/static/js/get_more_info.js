$(document).ready(function() {

    const $ = django.jQuery;

    const gmi = $("#get_more_info_btn");
    gmi.on('click', function (e) {
        get_more_info();
    })
});

const get_more_info = function () {
    const $ = django.jQuery;
    const label = $("#id_label").val();
    const info = $("#id_more_info");

    $.ajax({
        url:'/main/search?q='+label
    }).done(function (data) {
        try {
            var arr = JSON.parse(data);
            ingr = arr[0].food.nutrients
            info.text(JSON.stringify(ingr))
        }
        catch (e)
        {
            console.log(e)
        }
    })
}