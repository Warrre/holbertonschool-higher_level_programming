#!/usr/bin/node
const { argv } = require('node:process');

const size = parseInt(argv[2]);
if (size) {
  let i = 1;
  while (i <= size) {
    let j = 1;
    let ligne = '';
    while (j <= size) {
      ligne += 'X';
      j++;
    }
    console.log(ligne);
    i++;
  }
} else {
  console.log('Missing size');
}
