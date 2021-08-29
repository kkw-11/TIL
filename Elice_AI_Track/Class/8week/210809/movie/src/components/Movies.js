import axios from 'axios';
import React, { useEffect, useState } from 'react';
import Movie from './Movie';

function Movies() {
  const [movieList, setMovieList] = useState([]);
  async function fetch() {
    const response = await axios.get(
      'https://yts.mx/api/v2/list_movies.json?sort_by=year'
    );
    setMovieList(response.data.data.movies);
  }

  useEffect(() => {
    fetch();
  }, []);

  return (
    <ul>
      {movieList.map((movie) => {
        return (
          <Movie
            id={movie.id}
            title={movie.title}
            year={movie.year}
            rating={movie.rating}
          />
        );
      })}
    </ul>
  );
}

export default Movies;