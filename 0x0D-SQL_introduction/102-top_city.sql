-- This script displays the top 3 of cities temperature during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
Where month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
