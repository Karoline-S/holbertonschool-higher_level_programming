#!/usr/bin/node

exports.addMeMaybe = function (number, TheFunction) {
  if (typeof number === 'number') {
    TheFunction(number + 1);
  }
};
