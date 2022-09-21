$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'get',
  dataType: 'json'
})
  .done((data) => {
    $.each(data.results, function (index, film) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  });
