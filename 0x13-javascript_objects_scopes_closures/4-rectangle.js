#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c='X') {
    let columns = '';
    for (let i = 0; i < this.width; i++) {
      columns += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(columns);
    }
  }

  rotate () {
    const hold = this.height;
    this.height = this.width;
    this.width = hold;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
