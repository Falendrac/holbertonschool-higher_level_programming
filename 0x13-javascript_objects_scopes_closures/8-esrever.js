#!/usr/bin/node

/* returns the reversed version of a list */
exports.esrever = function (list) {
  const reverseList = [];

  for (let loop = 0, end = list.length - 1; loop < list.length; loop++, end--) {
    reverseList.push(list[end]);
  }

  return reverseList;
};
