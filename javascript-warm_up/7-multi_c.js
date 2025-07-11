#!/usr/bin/node
const { argv } = require('node:process');

const x = parseInt(argv[2]);
if (x) {
  let i = 1;
  while (i <= x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
