#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie

const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const recieved = JSON.parse(body);
    console.log(recieved.title);
  }
});
