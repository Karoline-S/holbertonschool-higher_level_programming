-- lists all records with a score >= 10
-- display score then name, ordered by highest score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
