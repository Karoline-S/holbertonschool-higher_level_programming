#!/usr/bin/node

const array = process.argv.splice(2);

if (array.length < 2) {
  console.log('0');
} else {
  array.sort(function (a, b) { return b - a; });
  console.log(array[1]);
}
