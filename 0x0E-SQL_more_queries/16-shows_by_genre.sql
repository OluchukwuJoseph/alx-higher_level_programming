-- This script lists all shows, and all genres linked to that show, from
-- the database hbtn_0d_tvshows.

SELECT tv_s.title, tv_g.name
FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres AS tv_s_g
ON tv_s.id = tv_s_g.show_id
LEFT JOIN tv_genres AS tv_g
ON tv_g.id = tv_s_g.genre_id
ORDER BY tv_s.title, tv_g.name;
