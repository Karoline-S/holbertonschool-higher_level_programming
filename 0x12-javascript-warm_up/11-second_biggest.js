#!/usr/bin/node

const array = process.argv;

if (array.length < 4) {
  console.log('0');
} else {
  array.sort();
  const twoBiggest = array.splice(array.length - 2);
  console.log(twoBiggest[0]);
}
