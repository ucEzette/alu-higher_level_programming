/* global $ */
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const films = data.results;
  films.forEach(function (film) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
