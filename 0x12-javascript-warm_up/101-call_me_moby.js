#!/usr/bin/node

exports.callMeMoby = function (x, TheFunction) {
  if (x < 0) { return; }
  while (x) {
    TheFunction();
    x--;
  }
};
