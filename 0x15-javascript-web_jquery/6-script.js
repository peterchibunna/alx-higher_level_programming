$(document).ready(function (e) {
  $('DIV#update_header').off('click').on('click', function (click) {
    $('header').text('New Header!!!')
  })
})
