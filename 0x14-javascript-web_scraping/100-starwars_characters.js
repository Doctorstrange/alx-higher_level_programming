#!/usr/bin/node

// script that prints all characters of a Star Wars movie

const req = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const recieved = JSON.parse(body);
  const characters = recieved.characters;
  for (const character of characters) {
    req(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const info = JSON.parse(body);
      console.log(info.name);
    });
  }
});
