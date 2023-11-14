#!/usr/bin/node
function add (x, y) {
  const z = y + x;
  console.log(z);
}

add(Number(process.argv[2]), Number(process.argv[3]));
