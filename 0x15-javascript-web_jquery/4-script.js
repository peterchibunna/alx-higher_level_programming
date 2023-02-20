$(document).ready(function (e) {
  $('DIV#toggle_header').off('click').on('click', function (click) {
    const header = $('header');
    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else {
      header.removeClass('green').addClass('red');
    }
  });
});
