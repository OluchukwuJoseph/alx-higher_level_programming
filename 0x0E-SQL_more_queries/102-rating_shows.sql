-- This script lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT tv_s.title, SUM(tv_r.rate) AS rating
FROM tv_shows AS tv_s
INNER JOIN tv_show_ratings AS tv_r
ON tv_s.id = tv_r.show_id
GROUP BY tv_s.title
ORDER BY rating DESC;
