#!/usr/bin/node

/**
 * This script computes the number of tasks completed by user id.
 */

const request = require('request');
const url = process.argv[2];
const taskStat = {};
let task;

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const taskStat = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!taskStat[todo.userId]) {
        taskStat[todo.userId] = 1;
      } else {
        taskStat[todo.userId] += 1;
      }
    }
  });
  console.log(taskStat);
});
