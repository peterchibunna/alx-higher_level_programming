#!/usr/bin/node

const myArgs = process.argv.slice(2);
// const numbers = [];

// for (let i = 0; i < myArgs.length; i++) {
//   numbers.push(parseInt(myArgs[i]));
// }
if (myArgs.length <= 1) {
  console.log(0);
} else {
  const args = myArgs.map(Number).sort((a, b) => a - b);
  console.log(args.sort().reverse()[1]);
}
