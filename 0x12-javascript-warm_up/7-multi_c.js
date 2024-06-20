#!/usr/bin/node

const firstArgument = parseInt(process.argv[2]);

if (isNaN(firstArgument)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArgument; i++) {
    console.log('C is fun');
  }
}
