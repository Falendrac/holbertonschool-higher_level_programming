#!/usr/bin/node
// script that write to the file, passes at argument
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (error, data) => {
  if (error) {
    return console.log(error);
  }
});
