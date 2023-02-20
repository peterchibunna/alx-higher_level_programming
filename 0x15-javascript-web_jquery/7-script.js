$(document).ready(function (e) {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function (person) {
    $('DIV#character').text(person.name);
  });
})
