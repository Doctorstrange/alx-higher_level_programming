#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const check = process.argv.slice(2).map(Number);
  const second_biggest = arr.sort(function (a, b) { return b - a; })[1];
  console.log(second_biggest);
}
