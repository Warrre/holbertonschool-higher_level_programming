#!/usr/bin/node
const { argv } = require('node:process');

function factorial (nombre) {
  if (nombre === 0) {
    return (1);
  }
  if (nombre < 0) {
    return (-1);
  }
  return (nombre * factorial(nombre - 1));
}
if (argv[2] === undefined) {
  console.log(1);
} else {
  const numb = parseInt(argv[2]);
  console.log(factorial(numb));
}
