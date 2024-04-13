#!/usr/bin/node

/*
 * This script prints two arguments passed to it,
 * in the following format: “ is ”
 */

const args = process.argv;
const arg1 = args[2];
const arg2 = args[3];

console.log(arg1 + ' is ' + arg2);
