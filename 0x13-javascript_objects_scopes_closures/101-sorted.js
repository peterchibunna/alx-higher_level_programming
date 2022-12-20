#!/usr/bin/node
const data = require('./101-data').dict;
const length = Object.keys(data).length;

Array.prototype.getUnique = function() {
  var o = {}, a = []
  for (var i = 0; i < this.length; i++) o[this[i]] = 1
  for (var e in o) a.push(e)
  return a
};
const newKeys = Object.values(data).getUnique();
let newDict = {};
for (let i = 0; i < newKeys.length; i++){
  newDict[newKeys[i]] = [];
  for (const property in data) {
    if (data[property] === Number(newKeys[i])){
      newDict[newKeys[i]].push(property);
    }
  }
}

console.log(newDict);
