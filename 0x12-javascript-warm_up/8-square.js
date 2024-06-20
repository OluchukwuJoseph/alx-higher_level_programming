#!/usr/bin/node

const firstArgument = parseInt(process.argv[2]);

if (isNaN(firstArgument)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArgument; i++) {
    for (let j = 0; j < firstArgument; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
