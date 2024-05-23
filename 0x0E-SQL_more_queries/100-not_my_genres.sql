-- This script uses the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter

SELECT DISTINCT tv_g.name
FROM tv_genres AS tv_g
INNER JOIN tv_show_genres AS tv_s_g
ON tv_g.id = tv_s_g.genre_id
WHERE tv_g.id NOT IN (
	SELECT tv_s_g.genre_id
	FROM tv_show_genres AS tv_s_g
	INNER JOIN tv_shows AS tv_s
	ON tv_s_g.show_id = tv_s.id
	WHERE tv_s.title = 'Dexter')
ORDER BY tv_g.name;
