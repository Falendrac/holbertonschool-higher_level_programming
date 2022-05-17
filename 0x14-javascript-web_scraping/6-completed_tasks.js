#!/usr/bin/node
/*
script that computes the number of tasks completed by user id.
*/
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    const users = {};
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].completed) {
        if (!(response.data[i].userId in users)) {
          users[response.data[i].userId] = 0;
        }
        users[response.data[i].userId] += 1;
      }
    }
    console.log(users);
  })
  .catch(function (error) {
    console.log(`code: ${error.response.status}`);
  })
  .then(function () { });
