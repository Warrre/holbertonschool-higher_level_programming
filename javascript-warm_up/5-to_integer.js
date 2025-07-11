#!/usr/bin/node

const arg = process.argv[2];
const conv = parseInt(arg);
if (isNaN(conv)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${conv}`);
}
