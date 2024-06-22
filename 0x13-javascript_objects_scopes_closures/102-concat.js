#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  const firstFile = process.argv[2];
  const secondFile = process.argv[3];
  const thridFile = process.argv[4];

  fs.readFile(firstFile, function (err, firstData) {
    if (err) {
      console.log(err);
      return;
    }
    fs.readFile(secondFile, function (err, secondData) {
      if (err) {
        console.log(err);
        return;
      }
      data = firstData.toString() + secondData.toString();
      fs.writeFile(thridFile, data, function (err) {
        if (err) {
          console.log(err);
          return;
        }
      })
    })
  })
}
