-- This script lists all records of the table second_table
-- List records
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
