#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/* Define a Square */
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let loop = 0; loop < this.height; loop++) {
      console.log(c.repeat(this.width));
    }
  }
};
