-- This script lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.

SELECT s.title, g.name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS s_g
ON s.id = s_g.show_id
LEFT JOIN tv_genres AS g
ON g.id = s_g.genre_id
ORDER BY s.title, g.name;
