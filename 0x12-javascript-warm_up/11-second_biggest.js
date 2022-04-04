#!/usr/bin/node

/* prints the addition of 2 integers */

const process = require('process');

const unique = (value, index, self) => {
  return self.indexOf(value) === index
}

const arrayCopy = process.argv.slice(2).filter(unique).map(function (item) {
  return parseInt(item);
});

console.log(arrayCopy.sort(function (a, b) { return b - a; })[1]);
