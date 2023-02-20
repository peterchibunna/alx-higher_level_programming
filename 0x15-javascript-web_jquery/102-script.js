$(document).ready(function (e) {
  const url = 'https://fourtonfish.com/hellosalut/';
  const language_code = $('INPUT#language_code');
  const btn_translate = $('INPUT#btn_translate');

  btn_translate.off('click').on('click', function (f) {
    fetchHello(url, language_code.val());
  });
  language_code.off('keyup').on('keyup', function (f) {
    if (f.keyCode === 13) {
      fetchHello(url, language_code.val());
    }
  });
});

const fetchHello = (url, language_code) => {
  $.get(`${url}?lang=${language_code}`, function (response) {
    $('DIV#hello').html(response.hello);
  })
};
