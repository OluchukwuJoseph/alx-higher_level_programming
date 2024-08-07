//  Fetch character name from external API
jQuery.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
function (data, textStatus) {
    $('DIV#character').text(data.name);
});
