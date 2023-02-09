#!/usr/bin/node
const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
req.get(url, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const response = JSON.parse(body);
  const dd = response.characters;
  for (const i of dd) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const response1 = JSON.parse(body1);
      console.log(response1.name);
    });
  }
});
