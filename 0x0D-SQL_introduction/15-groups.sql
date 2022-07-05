-- lists the number of records with the same score
-- db passed in as arg, table: second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
