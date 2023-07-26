#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log('Error:', err);
  } else if (response.statusCode === 200) {
    const employeeId = parseInt(process.argv[3]);
    const todos = JSON.parse(body);

    // Filter completed tasks for the given employee ID
    const completedTasks = todos.filter(task => task.completed && task.userId === employeeId);
    const totalTasks = todos.filter(task => task.userId === employeeId);

    const employeeName = completedTasks.length > 0 ? completedTasks[0].name : '';
    const numberOfCompletedTasks = completedTasks.length;
    const totalNumberOfTasks = totalTasks.length;

    console.log(`Employee ${employeeName} is done with tasks(${numberOfCompletedTasks}/${totalNumberOfTasks}):`);

    for (const task of completedTasks) {
      console.log(`\t${task.title}`);
    }
  } else {
    console.log('An error occurred. Status code:', response.statusCode);
  }
});

