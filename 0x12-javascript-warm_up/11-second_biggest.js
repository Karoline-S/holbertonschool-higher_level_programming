#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  let i = 2;
  const numArray = [];

  while (process.argv[i]) {
    numArray.push(Number(process.argv[i]));
    i++;
  }

  numArray.sort();
  const length = numArray.length;

  console.log(numArray[length - 2]);
}
