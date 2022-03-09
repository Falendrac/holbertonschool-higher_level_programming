-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id 
    FROM tv_show_genres RIGHT JOIN tv_shows on tv_show_genres.show_id = tv_shows.id
    WHERE tv_show_genres.show_id is NULL
    ORDER BY tv_shows.title, tv_show_genres.genre_id;
