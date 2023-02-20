$(document).ready(function (e) {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (response) {
    const films = response.results;
    for(var i = 0; i < films.length; i++){
      $('UL#list_movies').append('<li>'+films[i].title+'</li>');
    }
  });
})
