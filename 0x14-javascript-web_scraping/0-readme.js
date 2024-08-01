#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];

if (filename) {
  fs.readFile(filename, 'utf8', function (err, file) {
    if (err) {
      console.log(err);
    } else {
      console.log(file);
    }
  });
}
