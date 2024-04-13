#!/usr/bin/node

let firstArg = parseInt(process.argv[2]);

if (!isNaN(firstArg)) {
  while (firstArg > 0) {
    console.log('C is fun');
    firstArg--;
  }
} else {
  console.log('Missing number of occurrences');
}
