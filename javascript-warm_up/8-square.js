#!/usr/bin/node

const SizeSquare = parseInt(process.argv[2]);

if (isNaN(SizeSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < SizeSquare; i++) {
    console.log('X'.repeat(SizeSquare));
  }
}

