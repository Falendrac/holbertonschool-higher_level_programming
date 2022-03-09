-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name
    FROM tv_show_genres
    RIGHT JOIN tv_shows on tv_show_genres.show_id = tv_shows.id 
    RIGHT JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
    ORDER BY tv_shows.title, tv_genres.name;
