#!/usr/bin/node

/**
 * This script prints the number of movies where “Wedge Antilles” is present
 */

const request = require('request');
const characterId = '18/';
const url = process.argv[2];
let count = 0;
let movie;
let character;

request(url, (error, response, body) => {
  if (error) {
    console.log(`An error occured: ${error}`);
  } else {
    const movies = JSON.parse(body);

    for (movie of movies.results) {
      for (character of movie.characters) {
        if (character.endsWith(characterId)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
