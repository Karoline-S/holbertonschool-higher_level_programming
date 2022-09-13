#!/usr/bin/node

const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    const movies = response.data.results;
    let count = 0;
    movies.forEach(dict => {
      if (dict.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count += 1;
      }
    });
    console.log(count);
  });
