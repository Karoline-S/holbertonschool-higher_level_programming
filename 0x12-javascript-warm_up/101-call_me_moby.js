#!/usr/bin/node

exports.callMeMoby = function (x, TheFunction) {
  while (x) {
    TheFunction();
    x--;
  }
};
