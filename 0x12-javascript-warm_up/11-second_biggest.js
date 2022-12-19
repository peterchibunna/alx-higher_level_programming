#!/usr/bin/node

const myArgs = process.argv.slice(2);
const numbers = [];

// for (let i = 0; i < myArgs.length; i++) {
//   numbers.push(parseInt(myArgs[i]));
// }
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  console.log(myArgs.sort().reverse()[1]);
}
