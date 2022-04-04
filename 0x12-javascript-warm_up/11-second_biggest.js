#!/usr/bin/node

/* prints the addition of 2 integers */

const process = require('process');

const arrayCopy = process.argv.slice(2).map(function (item) {
  return parseInt(item);
});

arrayCopy.sort();

console.log(arrayCopy[arrayCopy.length - 2]);
