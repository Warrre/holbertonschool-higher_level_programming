#!/usr/bin/node

const arg = process.argv[2];
const convArg = Number(arg);
if (isNaN(convArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convArg; i++) {
    console.log('C is fun');
  }
}
