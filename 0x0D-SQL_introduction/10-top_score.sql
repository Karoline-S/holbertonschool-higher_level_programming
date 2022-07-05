-- lists all records in table ordered by top score
-- display score then name for each row
-- db passed in as arg, table: second_table
SELECT score, name
FROM second_table
ORDER BY score DESC;
