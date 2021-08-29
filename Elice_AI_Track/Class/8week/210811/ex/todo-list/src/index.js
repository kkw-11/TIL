import { createStore } from 'redux';

const form = document.querySelector('form');
const input = document.querySelector('input');
const ul = document.querySelector('ul');

// Action Types
const ADD_TODO = 'ADD_TODO';
const DELETE_TODO = 'DELETE_TODO';
const DONE_TODO = 'DONE_TODO';

// Action Creaters
const addToDo = (text) => {
  return {
    type: ADD_TODO,
    text,
  };
};

const deleteTodo = (id) => {
  return {
    type: DELETE_TODO,
    id,
  };
};

const doneTodo = (id) => {
  return {
    type: DONE_TODO,
    id,
  };
};

// Reducer
const reducer = (state = [], action) => {
  switch (action.type) {
    case ADD_TODO:
      return [{ text: action.text, id: Date.now(), done: false }, ...state];
    case DELETE_TODO:
      return state.filter((toDo) => toDo.id !== action.id);
    case DONE_TODO:
      const doneTodo = Object.assign(
        {},
        state.find((toDo) => toDo.id === action.id)
      );
      doneTodo.done = true;
      return [...state.filter((toDo) => toDo.id !== action.id), doneTodo];
    default:
      return state;
  }
};

// Store
const store = createStore(reducer);

// Dispatch
const dispatchAddTodo = (text) => {
  store.dispatch(addToDo(text));
};

const dispatchDeleteTodo = (id) => {
  store.dispatch(deleteTodo(id));
};

const dispatchDoneTodo = (id) => {
  store.dispatch(doneTodo(id));
};

// Function for subscribe ( when state change )
const createToDos = () => {
  const toDos = store.getState();
  ul.innerHTML = '';
  toDos.forEach((toDo) => {
    const li = document.createElement('li');
    const btn = document.createElement('button');
    btn.innerText = 'Delete';
    btn.addEventListener('click', () => dispatchDeleteTodo(toDo.id));
    li.id = toDo.id;
    li.innerText = toDo.text;
    li.appendChild(btn);
    ul.appendChild(li);
    if (toDo.done) {
      li.style.textDecoration = 'line-through';
    } else {
      const done = document.createElement('button');
      done.innerText = 'Done';
      done.addEventListener('click', () => dispatchDoneTodo(toDo.id));
      li.appendChild(done);
    }
  });
};

// Subscribe
store.subscribe(createToDos);

const onSubmit = (e) => {
  e.preventDefault();
  const toDo = input.value;
  input.value = '';
  dispatchAddTodo(toDo);
};

form.addEventListener('submit', onSubmit);