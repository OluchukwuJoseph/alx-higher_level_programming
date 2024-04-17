-- This script lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT title
FROM tv_shows
WHERE ID IN (
	SELECT show_id
	FROM tv_show_genres
	WHERE genre_id = (
		SELECT id
		FROM tv_genres
		WHERE name = 'comedy'
		)
	)
ORDER BY title;
