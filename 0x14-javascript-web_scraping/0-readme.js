#!/usr/bin/node
// script that reads and prints the content of a file, passes at argument
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (error, data) => {
  if (error) {
    return console.log(error);
  }
  console.log(data.toString());
});
