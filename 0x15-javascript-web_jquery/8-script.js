// Fetches and lists the title for all movies from an external API
$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
function (data, textStatus) {
    for (film of data.results) {
        $('UL#list_movies').append(`<li>${film.title}</li>`);
    }
});
