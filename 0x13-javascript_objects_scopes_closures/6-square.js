#!/usr/bin/node

const Square2 = require('./5-square');

class Square extends Square2 {

  charPrint (ch) {
    const symbol = ch !== undefined ? ch : 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(symbol.repeat(this.width));
    }
  }
}

module.exports = Square;
