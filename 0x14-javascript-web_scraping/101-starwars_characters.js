#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const displayCharacters = (characters, index) => {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        displayCharacters(characters, index + 1);
      }
    }
  });
};

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    displayCharacters(characters, 0);
  }
});
