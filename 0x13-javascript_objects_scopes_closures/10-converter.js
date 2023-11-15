#!/usr/bin/node

exports.converter = function (base) {
  return function (numinbase) {
    return numinbase.toString(base);
  };
};
