#!/usr/bin/node
const data = require('./101-data').dict;

const getUnique = function (arr) {
  const o = {};
  const a = [];
  for (let i = 0; i < arr.length; i++) o[arr[i]] = 1;
  for (const e in o) a.push(e);
  return a;
};
const newKeys = getUnique(Object.values(data));
const newDict = {};
for (let i = 0; i < newKeys.length; i++) {
  newDict[newKeys[i]] = [];
  for (const property in data) {
    if (data[property] === Number(newKeys[i])) {
      newDict[newKeys[i]].push(property);
    }
  }
}

console.log(newDict);
