// fetch and display a translation of "Hello" based on user input
$(document).ready(() => {
    $('INPUT#btn_translate').click(fetchTranslation);
    $('INPUT#language_code').keyup(function (event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        const lang = $('INPUT#language_code').val();
        $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${lang}`,
        function (data, textContent) {
            $('DIV#hello').text(data.hello);
        }).fail(function() {
            $('DIV#hello').text('Error fetching translation');
        });
    }
});
