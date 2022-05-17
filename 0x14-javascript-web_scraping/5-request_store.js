#!/usr/bin/node
/*
script that gets the contents of a webpage and stores it in a file.
*/
const axios = require('axios').default;
const fs = require('fs');

axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, 'utf8', (error) => {
      if (error) {
        return console.log(error);
      }
    });
  })
  .catch(function (error) {
    console.log(`code: ${error.response.status}`);
  })
  .then(function () { });
