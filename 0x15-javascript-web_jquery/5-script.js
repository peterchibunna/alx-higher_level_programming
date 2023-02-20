$(document).ready(function (e) {
  $('DIV#add_item').off('click').on('click', function (click) {
    $('UL.my_list').append('<li>Item</li>')
  })
})
