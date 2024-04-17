-- This script lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT shows.title, SUM(show_ratings.rate) AS 'rating'
FROM tv_shows AS shows
INNER JOIN tv_show_ratings AS show_ratings
ON shows.id = show_ratings.show_id
GROUP BY shows.title
ORDER BY rating DESC;
