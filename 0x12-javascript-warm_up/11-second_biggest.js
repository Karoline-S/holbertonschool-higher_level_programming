#!/usr/bin/env node

if (process.argv.length < 4) {
  console.log('0');
} else {
  let i = 2;
  const numArray = [];

  while (process.argv[i]) {
    numArray.push(Number(process.argv[i]));
    i++;
  }

  let biggest = numArray[0];
  let nextBiggest = numArray[0];

  for (i = 0; i < numArray.length; i++) {
    if (numArray[i] > biggest) {
      nextBiggest = biggest;
      biggest = numArray[i];
    } else if (numArray[i] > nextBiggest) {
      nextBiggest = numArray[i];
    }
  }
  console.log(nextBiggest);
}
