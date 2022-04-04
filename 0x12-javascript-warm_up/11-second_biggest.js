#!/usr/bin/node

/* prints the addition of 2 integers */

const process = require('process');

let highest = 0;
let second = 0;

const arrayCopy = process.argv.slice(2).map(function (item) {
  return parseInt(item);
});

for (let loop = 0; loop < arrayCopy.length; loop++) {
  if (highest < arrayCopy[loop]) {
    second = highest;
    highest = arrayCopy[loop];
  } else if (second < arrayCopy[loop]) {
    second = arrayCopy[loop];
  }
}

console.log(second);
