-- This script lists all genres in the database
-- hbtn_0d_tvshows_rate by their rating.

SELECT genre.name, SUM(show_ratings.rate) AS 'rating'
FROM tv_genres AS genre
INNER JOIN tv_show_genres AS show_genre
ON genre.id = show_genre.genre_id
INNER JOIN tv_show_ratings AS show_ratings
ON show_ratings.show_id = show_genre.show_id
GROUP BY genre.name
ORDER BY rating DESC;
