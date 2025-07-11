#!/usr/bin/node
const { argv } = require('node:process');

if (argv[3] === undefined) {
  console.log(0);
} else {
  let i = 2;
  let one = 0;
  let seconde = 0;
  while (i < argv.length) {
    if (one < Number(argv[i])) {
      seconde = one;
      one = Number(argv[i]);
    }
    if (seconde < Number(argv[i]) && Number(argv[i]) < one) {
      seconde = Number(argv[i]);
    }
    i++;
  }
  console.log(seconde);
}
