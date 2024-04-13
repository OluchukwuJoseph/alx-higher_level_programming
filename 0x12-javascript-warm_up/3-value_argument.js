#!/usr/bin/node

/*
 * This script prints the first argument passed to it
 */

const arg2 = process.argv[2];

if (arg2 !== undefined) {
  console.log(arg2);
} else {
  console.log('No argument');
}
