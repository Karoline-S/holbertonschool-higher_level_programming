$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  type: 'get',
  dataType: 'json'
})
  .done((data) => {
    $('DIV#character').text(data.name);
  });
