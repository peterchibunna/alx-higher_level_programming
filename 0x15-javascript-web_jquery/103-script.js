$(document).ready(function (e) {
  const url = 'https://fourtonfish.com/hellosalut/';
  const languageCode = $('INPUT#language_code');
  const btnTranslate = $('INPUT#btn_translate');

  btnTranslate.off('click').on('click', function (f) {
    fetchHello(url, languageCode.val());
  });
  languageCode.off('keyup').on('keyup', function (f) {
    if (f.keyCode === 13) {
      fetchHello(url, languageCode.val());
    }
  });
});

const fetchHello = (url, languageCode) => {
  $.get(`${url}?lang=${languageCode}`, function (response) {
    $('DIV#hello').html(response.hello);
  });
};
