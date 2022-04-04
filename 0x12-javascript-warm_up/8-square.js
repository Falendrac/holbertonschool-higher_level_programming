#!/usr/bin/node

/* prints a square */

const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let loop = 0; loop < Number(process.argv[2]); loop++) {
    console.log('X'.repeat(Number(process.argv[2])));
  }
}
