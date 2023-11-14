#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const check = process.argv.slice(2).map(Number);
  const second_biggest = check.sort(function (x, y) { return y - x; })[1];
  console.log(second);
}
