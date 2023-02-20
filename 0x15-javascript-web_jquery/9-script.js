$(document).ready(function (e) {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (response) {
    // resource is blocked! with cors! no Access-Control-Allow-Origin in the response header
    // we cannot access the response
    $('DIV#hello').text(response.hello);
  });
})
