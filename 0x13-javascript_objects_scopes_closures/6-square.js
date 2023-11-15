#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      let square = '';
      for (let y = 0; y < this.width; y++) {
        square += c;
      }
      console.log(square);
    }
  }
}

module.exports = Square;
