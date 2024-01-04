#!/usr/bin/node

// script that gets the contents of a webpage and stores it in a file

const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filepath, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
