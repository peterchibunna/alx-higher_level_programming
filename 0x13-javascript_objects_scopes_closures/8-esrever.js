#!/usr/bin/node

exports.esrever = function (list) {
  const size = list.length;
  let newList = Array();
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
