#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let count = parseInt(process.argv[2]);
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
