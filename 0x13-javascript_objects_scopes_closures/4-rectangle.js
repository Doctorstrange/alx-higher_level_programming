#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let rec = '';
      for (let y = 0; y < this.width; y++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }

  rotate () {
    const ex = this.width;
    this.width = this.height;
    this.height = ex;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
