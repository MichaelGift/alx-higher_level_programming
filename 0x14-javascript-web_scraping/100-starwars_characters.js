#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) return;
  const characters = JSON.parse(body).characters;
  printCharacters(characters);
});

function printCharacters (characters) {
  characters.forEach((character) => {
    request(character, (error, response, body) => {
      if (error) return;
      console.log(JSON.parse(body).name);
    });
  });
}
