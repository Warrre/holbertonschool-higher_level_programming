#!/usr/bin/node

const argCount = process.argv[2];
if (!argCount) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
