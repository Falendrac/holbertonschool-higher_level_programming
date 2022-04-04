#!/usr/bin/node

/* prints the addition of 2 integers */

const process = require('process');

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }

  if (a === 0 || a === 1) {
    return 1;
  }

  return a * factorial(a - 1);
}

console.log(factorial(Number(process.argv[2])));
