#!/usr/bin/node

exports.esrever = function (list) {
  const length = list.length;
  let holdItem = '';

  for (let i = 0; i < length / 2; i++) {
    holdItem = list[i];
    list[i] = list[length - 1 - i];
    list[length - 1 - i] = holdItem;
  }
  return list;
};
