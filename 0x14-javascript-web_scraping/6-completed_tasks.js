#!/usr/bin/node

/**
 * This script computes the number of tasks completed by user id.
 */

const request = require('request');
const url = process.argv[2];
const taskStat = {};
let task;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(`An error occured: ${error}`);
  }
  for (task of body) {
    if (!taskStat[task.userId]) {
      taskStat[task.userId] = 0;
    }
    if (task.completed) {
      taskStat[task.userId]++;
    }
  }
  console.log(taskStat);
});
