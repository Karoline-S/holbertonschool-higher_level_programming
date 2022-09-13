#!/usr/bin/node

const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url)
  .then(function (response) {
    const characters = response.data.characters;
    for (let i = 0; i < characters.length; i++) {
      getName(characters[i]);
    }
  });

function getName (item) {
  axios.get(item)
    .then(function (resp) {
      console.log(resp.data.name);
    });
}
