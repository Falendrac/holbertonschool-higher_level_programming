#!/usr/bin/node

/* Define the class Rectangle */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let loop = 0; loop < this.height; loop++) {
      console.log('X'.repeat(this.width));
    }
  }
};
