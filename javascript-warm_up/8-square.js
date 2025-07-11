#!/usr/bin/node

const arg = process.argv[2];
const convArg = Number(arg);
if ((isNaN(convArg)) || convArg <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convArg; i++) {
    console.log('X'.repeat(convArg));
  }
}
