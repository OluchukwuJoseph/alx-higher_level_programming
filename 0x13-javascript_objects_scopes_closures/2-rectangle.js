#!/usr/bin/node

// This module contains a class `Rectangle`

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number') {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }
}

module.exports = Rectangle;
