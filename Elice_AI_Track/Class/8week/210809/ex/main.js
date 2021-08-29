// node.js es6 문법을 지원을 안해요.
// 그래서 babel 을 설치해여하는데.. 굳이
const axios = require('axios');

const post = async () => {
  const url = 'https://reqres.in/api/login';
  const user = {
    email: 'eve.holt@reqres.in',
    password: 'cityslicka',
  };

  // axios.post(url, user).then((response) => {
  //   console.log(response);
  //   console.log(response.status);
  //   console.log(response.data);
  // });
  const { status, data } = await axios.post(url, user);
  console.log(status);
  console.log(data);
};

const get = async () => {
  const url = 'https://reqres.in/api/users/2';
  // axios.get(url).then((response) => {
  //   console.log(response.status);
  //   console.log(response.data);
  // });
  const response = await axios.get(url);

  console.log(response.status);
  console.log(response.data);
};

const put = async () => {
  const url = 'https://reqres.in/api/users/2';
  const data = {
    first_name: 'White',
    last_name: 'Rabbit',
    email: 'alice@elice.io',
  };

  const response = await axios.put(url, data);
  console.log(response.status);
  console.log(response.data);
};

const deleteFn = async () => {
  const url = 'https://reqres.in/api/users/2';
  const response = await axios.delete(url);

  console.log(response.status);
};

// (async () => {
//   await post();
//   await get();
// })();
// // 즉시실행함수 iife

deleteFn();