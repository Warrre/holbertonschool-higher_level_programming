#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length >= 4) {
  console.log('Arguments found');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
