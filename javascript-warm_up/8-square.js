#!/usr/bin/node
const arg = process.argv[2];
const convArg = parseInt(arg);
if (isNaN(convArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convArg; i++) {
    console.log('X'.repeat(convArg));
  }
}
