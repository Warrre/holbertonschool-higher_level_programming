#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length === 3) {
  console.log(NaN);
} else {
  const a = parseInt(argv[2]);
  const b = parseInt(argv[3]);
  console.log(a + b);
}
