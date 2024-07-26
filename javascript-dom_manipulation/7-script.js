document.addEventListener('DOMContentLoaded', function () {
  const ListMovies = document.getElementById('list_movies');
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
        for (const movie of data.results) {
            const item = document.createElement('li');
            item.textContent = movie.title;
            ListMovies.appendChild(item);
        }
    });
});
