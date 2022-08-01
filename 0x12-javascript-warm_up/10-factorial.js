#!/usr/bin/node

let num = Number(process.argv[2]);

if (!num) { num = 1; }

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(num));
