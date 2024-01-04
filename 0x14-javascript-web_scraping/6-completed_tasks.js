#!/usr/bin/node

// computes the number of tasks completed by user id

const req = require('request');
const url = process.argv[2];

req.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const comptask = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (comptask[todo.userId] === undefined) {
        comptask[todo.userId] = 1;
      } else {
        comptask[todo.userId] += 1;
      }
    }
  });
  console.log(comptask);
});
