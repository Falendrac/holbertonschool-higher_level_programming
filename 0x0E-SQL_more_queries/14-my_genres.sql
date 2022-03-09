-- lists all genres of the show Dexter.
SELECT tv_genres.name
    FROM tv_show_genres
    JOIN tv_shows on tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres on tv_genres.id = tv_show_genres.genre_id
    WHERE tv_shows.title = "Dexter"
    ORDER BY tv_genres.name;
