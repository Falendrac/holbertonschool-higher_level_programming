#!/usr/bin/node

/* prints the addition of 2 integers */

const process = require('process');

function add (a, b) {
  console.log(a + b);
}

add(Number(process.argv[2]), Number(process.argv[3]));
