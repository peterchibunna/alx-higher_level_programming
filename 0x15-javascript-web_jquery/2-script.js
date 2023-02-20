$(document).ready(function (e) {
  $('div#red_header').off('click').on('click', function (event) {
    $('header').css({'color': '#FF0000'})
  })
})
