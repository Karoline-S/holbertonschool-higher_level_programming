#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
console.log(url);
axios.get(url)
  .then(function (response) {
    console.log(response.data.title);
  });
