#!/usr/bin/node

/**
 * This script gets the contents of a webpage and stores it in a file.
 */

const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.log(`An error occured: ${error}`);
  } else {
    fs.writeFile(filename, body, 'utf-8', (error) => {
      if (error) {
        console.log(`An error occured: ${error}`);
      }
    });
  }
});
