#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

function factorial (num) {
  if (num === 0) {
    return 0;
  }

  return num + factorial(num - 1);
}

if (isNaN(firstArg)) {
  console.log(1);
} else {
  console.log(factorial(firstArg));
}
