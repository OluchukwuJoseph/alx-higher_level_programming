-- This script lists all genres by their rating.

SELECT tv_g.name, SUM(tv_r.rate) AS rating
FROM tv_genres AS tv_g
INNER JOIN tv_show_genres AS tv_s_g
ON tv_g.id = tv_s_g.genre_id
INNER JOIN tv_show_ratings AS tv_r
ON tv_r.show_id = tv_s_g.show_id
GROUP BY tv_g.name
ORDER BY rating DESC;
