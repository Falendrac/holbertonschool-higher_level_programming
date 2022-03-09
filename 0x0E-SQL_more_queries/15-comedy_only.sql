-- lists all genres of the show Dexter.
SELECT tv_shows.title
    FROM tv_show_genres
    JOIN tv_shows on tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres on tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = "Comedy"
    ORDER BY tv_shows.title;
