// fetch and display a translation of "Hello" based on user input
$(document).ready(() => {
    $('INPUT#btn_translate').click(() => {
        lang = $('INPUT#language_code').val();
        $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${lang}`,
        function (data, textContent) {
            $('DIV#hello').text(data.hello);
        }).fail(function() {
            $('DIV#hello').text('Error fetching translation');
        });
    });
});
