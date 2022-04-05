#!/usr/bin/node

/* Return the occurences in a list */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let loop = 0; loop < list.length; loop++) {
    if (list[loop] === searchElement) {
      count++;
    }
  }

  return count;
};
