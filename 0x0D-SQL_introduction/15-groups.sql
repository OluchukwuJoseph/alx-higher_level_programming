-- lists the number of records with the same score in the table second_table.
-- list record
SELECT DISTINCT score,
COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
