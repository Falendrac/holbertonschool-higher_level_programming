#!/usr/bin/node

/* prints the first argument passed to it */

import process from 'process';

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}