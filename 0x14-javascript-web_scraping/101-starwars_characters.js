#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
let characters = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const recieved = JSON.parse(body);
  characters = recieved.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const info = JSON.parse(body);
    console.log(info.name);
    getCharacters(index + 1);
  });
};
