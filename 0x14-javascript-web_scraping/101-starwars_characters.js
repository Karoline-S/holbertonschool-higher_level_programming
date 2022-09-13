#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url)
  .then(function (response) {
    for (const item of response.data.characters) {
      getName(item);
    }
  });

function getName (item) {
  axios.get(item)
    .then(function (resp) {
      console.log(resp.data.name);
    });
}
