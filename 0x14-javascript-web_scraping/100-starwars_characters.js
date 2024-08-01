#!/usr/bin/node

/**
 * This script prints all characters of a Star Wars movie
 */

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
let character;

request(url, (error, response, body) => {
  if (error) {
    console.log(`An error occured: ${error}`);
  } else {
    const characters = JSON.parse(body).characters;

    for (character of characters) {
      request(character, (err, characterResponse, characterBody) => {
        if (err) {
          console.log(`An error occured: ${err}`);
        } else {
          const person = JSON.parse(characterBody);
          console.log(person.name);
        }
      });
    }
  }
});
