#!/usr/bin/node

/* prints two arguments passed to it, in the following format: “ is ” */

import process from 'process';

console.log(process.argv[2] + ' is ' + process.argv[3]);