#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      n += 1;
    }
  });
  return n;
};
