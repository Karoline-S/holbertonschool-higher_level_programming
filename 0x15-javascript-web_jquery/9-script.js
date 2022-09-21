$(document).ready(() => {
  $.ajax({
    url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
    type: 'get',
    dataType: 'json'
  })
    .done((data) => {
      console.log(data);
      console.log(data.hello);
      $('DIV#hello').text(data.hello);
    });
});
