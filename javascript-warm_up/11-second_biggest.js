#!/usr/bin/node

const arg = process.argv.slice(2);
if (arg.length <= 1) {
  console.log(0);
  process.exit();
}
const convArg = arg.map(Number);
convArg.sort((a, b) => b - a);
console.log(convArg[1])
