import React from 'react';

function Movie({ id, title, year, rating }) {
  return (
    <li key={id}>
      <p>제목:{title}</p>
      <p>개봉:{year}</p>
      <p>평정:{rating}</p>
    </li>
  );
}

export default Movie;