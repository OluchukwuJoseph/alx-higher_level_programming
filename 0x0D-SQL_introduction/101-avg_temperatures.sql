-- This script displays the average temperature by city ordered by temperature
SELECT DISTINCT city, AVG(value) AS avg_values
FROM temperatures
GROUP BY city
ORDER BY avg_values DESC;
