#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/* Define a Square */
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
