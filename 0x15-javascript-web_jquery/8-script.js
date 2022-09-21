$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'get',
  dataType: 'json'
})
  .done((data) => {
    console.log(data.results);
    $.each(data.results, function (index, film) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  });
