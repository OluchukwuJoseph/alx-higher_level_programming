-- This script lists all the record with score >= 10
-- List records
SELECT score, name
FROM second_table
where score >= 10
ORDER BY score DESC;
