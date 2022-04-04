#!/usr/bin/node

/* prints x times “C is fun
Where x is the first argument of the script
*/

import process from 'process';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let loop = 0; loop < Number(process.argv[2]); loop++) {
    console.log('C is fun');
  }
}
