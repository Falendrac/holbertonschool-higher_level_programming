#!/usr/bin/node
/*
 script that prints the number of movies
 where the character “Wedge Antilles” is present.
*/
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    let count = 0;
    for (const film of response.data.results) {
      for (const actors of film.characters) {
        if (actors.includes('people/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () { });
