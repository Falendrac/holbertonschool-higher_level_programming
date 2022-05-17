#!/usr/bin/node
/*
 script that prints the number of movies
 where the character “Wedge Antilles” is present.
*/
const axios = require('axios').default;
let count = 0;

axios.get(process.argv[2])
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      if (response.data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log(`code: ${error.response.status}`);
  })
  .then(function () { });
