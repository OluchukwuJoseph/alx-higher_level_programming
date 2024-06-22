#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let j = list.length - 1;

  for (let i = 0; i < list.length; i++, j--) {
    newList[i] = list[j];
  }

  return newList;
};
