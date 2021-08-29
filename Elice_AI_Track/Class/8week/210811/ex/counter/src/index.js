import { createStore } from 'redux';
const add = document.getElementById('add');
const minus = document.getElementById('minus');
const number = document.querySelector('span');

// Action Type
const ADD = 'ADD';
const MINUS = 'MINUS';

// Action Creator
const addAction = () => {
  return {
    type: ADD,
  };
};

const minusAction = () => {
  return {
    type: MINUS,
  };
};

// Reducer
const reducer = (state = 0, action) => {
  switch (action.type) {
    case ADD:
      return state + 1;
    case MINUS:
      return state - 1;
    default:
      return state;
  }
};

// Store
const store = createStore(reducer);

// Dispatch
add.addEventListener('click', () => store.dispatch(addAction()));
minus.addEventListener('click', () => store.dispatch(minusAction()));

// Subscribe
store.subscribe(() => {
  number.innerText = store.getState();
});

/*
  1. dispatch에 action creator 만든 action을 넘겨주면
  2. reducer 작동하고.
  3. reducer 작동에 따라, 값이 변경되면 subscribe가 작동.
*/


// let counter = 0;
// number.innerText = counter;
// const onChange= () =>{
//   number.innerText = counter;
// }

// const handleAdd = () =>{
//   counter += 1;
//   number.innerText = counter;
//   onChange();
// }

// const handleMinus = () =>{
//   counter -= 1;
//   number.innerText =counter;
//   onChange();

// }

// add.addEventListener('click', handleAdd);
// minus.addEventListener('click', handleMinus);