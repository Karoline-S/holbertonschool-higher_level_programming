#!/usr/bin/node

let repeats = Number(process.argv[2]);

if (!repeats) {
  console.log('Missing number of occurrences');
} else {
  if (repeats > 0) {
    while (repeats) {
      console.log('C is fun');
      repeats--;
    }
  }
}
