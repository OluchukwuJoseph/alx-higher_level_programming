#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
}

module.exports = Square;
