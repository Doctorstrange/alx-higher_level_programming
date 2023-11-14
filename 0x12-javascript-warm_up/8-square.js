#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const length = Number(process.argv[2]);
  let breath = 0;
  while (breath < length) {
    console.log('X'.repeat(length));
    breath++;
  }
}
