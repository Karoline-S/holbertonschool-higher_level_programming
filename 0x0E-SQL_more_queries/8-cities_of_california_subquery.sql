-- lists all cities connected to a state in the db
-- db passed in as arg
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
    )
ORDER BY id ASC