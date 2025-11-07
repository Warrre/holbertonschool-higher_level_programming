#!/usr/bin/node

function Factorial (n) {
  if (isNaN(n) || n < 1) {
    return 1;
  }
  return n * Factorial(n - 1);
}

console.log(Factorial(parseInt(process.argv[2])));

