// Fetches from an external API and displays the value of hello from that fetch
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
function (data, textStatus) {
    $('DIV#hello').text(data.hello);
});
