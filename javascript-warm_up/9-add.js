#!/usr/bin/node

const arg1 = process.argv[2];
const convArg1 = Number(arg1);
const arg2 = process.argv[3];
const convArg2 = Number(arg2);
function add (a, b) {
  return a + b;
}
const result = add(convArg1, convArg2);
console.log(result);
