#!/usr/bin/node

const arg = process.argv[2];
const conv = Number(arg);
if (isNaN(conv)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${conv}`);
}
