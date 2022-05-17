#!/usr/bin/node
/*
script that prints the title of a Star Wars
movie where the episode number matches a given integer.
*/
const axios = require('axios').default;
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

axios.get(url)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(`code: ${error.response.status}`);
  })
  .then(function () { });
