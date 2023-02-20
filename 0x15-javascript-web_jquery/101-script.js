$(document).ready(function (e) {
  const list = $('UL.my_list');
  $('DIV#add_item').on('click', function (click) {
    list.append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function (click) {
    list.find('li').last().remove();
  });
  $('DIV#clear_list').on('click', function (click) {
    list.html('');
  });

})
