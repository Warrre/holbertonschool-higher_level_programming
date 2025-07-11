#!/usr/bin/node

const arg = process.argv[2];
const convArg = Number(arg);
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(convArg));
