#!/usr/bin/node
const fs = require('fs');
const request = require('request');
let url = process.argv[2];
let fileName = process.argv[3];
request(url).pipe(fs.createWriteStream(fileName));
