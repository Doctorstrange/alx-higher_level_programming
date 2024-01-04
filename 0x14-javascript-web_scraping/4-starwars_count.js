#!/usr/bin/node
// number of movies where the character “Wedge Antilles” is present

const req = require('request');
const url = process.argv[2];
const characterId = '18';
let num = 0;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const recieved = JSON.parse(body);
    recieved.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
