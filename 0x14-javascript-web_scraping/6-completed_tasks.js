#!/usr/bin/node

/**
 * This script computes the number of tasks completed by user id.
 */

const request = require('request');
const url = process.argv[2];
const taskStat = {};
let task;

request(url, (error, response, body) => {
  if (error) {
    console.log(`An error occured: ${error}`);
  }
  const tasks = JSON.parse(body);
  for (task of tasks) {
    if (!taskStat[task.userId]) {
      taskStat[task.userId] = 0;
    }
    if (task.completed === true) {
      taskStat[task.userId]++;
    }
  }

  console.log(taskStat);
});
