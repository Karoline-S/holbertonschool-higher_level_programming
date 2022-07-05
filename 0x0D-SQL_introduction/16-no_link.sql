-- lists all records of the table except rows without name
-- display score then name
-- db passed in as arg, table: second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
