#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const pair in dict) {
  if (!newDict[dict[pair]]) {
    newDict[dict[pair]] = [];
  }
  newDict[dict[pair]].push(pair);
}

console.log(newDict);
