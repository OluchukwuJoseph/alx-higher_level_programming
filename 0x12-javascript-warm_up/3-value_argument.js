#!/usr/bin/node

const argv = process.argv;
const arg = argv[2];

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
