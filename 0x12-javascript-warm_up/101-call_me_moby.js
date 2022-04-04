#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let loop = 0; loop < x; loop++) {
    theFunction();
  }
};
