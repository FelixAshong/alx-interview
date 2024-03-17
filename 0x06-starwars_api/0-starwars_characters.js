#!/usr/bin/node
/**
  prints all characters of a Star Wars movie
  */

const myArgs = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];

request(url, async function (error, response, body) {
  if (!error) {
    const json = JSON.parse(body);
    const endpoints = json.characters;
    for (const endpoint of endpoints) {
      await new Promise(function (resolve, reject) {
        request(endpoint, function (error, response, body) {
          if (!error) {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});
