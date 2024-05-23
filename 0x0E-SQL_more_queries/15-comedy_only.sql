-- This script lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT tv_s.title
FROM tv_genres AS tv_g
INNER JOIN tv_show_genres AS tv_s_g
ON tv_g.id = tv_s_g.genre_id
INNER JOIN tv_shows AS tv_s
ON tv_s.id = tv_s_g.show_id
WHERE tv_g.name = 'Comedy'
ORDER BY tv_s.title;
