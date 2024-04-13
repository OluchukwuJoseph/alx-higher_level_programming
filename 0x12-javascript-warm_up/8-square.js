#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

if (!isNaN(firstArg)) {
  let i = 0;
  while (i < firstArg) {
    for (let j = 0; j < firstArg; j++) {
      process.stdout.write('X');
    }
    console.log('');
    i++;
  }
} else {
  console.log('Missing size');
}
