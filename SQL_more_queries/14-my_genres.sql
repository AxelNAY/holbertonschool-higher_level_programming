SELECT tv_genres.name AS name FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show
ON tv_show_genres.id = tv_show.id
WHERE tv_show.title = 'Dexter'
ORDER BY name ASC;