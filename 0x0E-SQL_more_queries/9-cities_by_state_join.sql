-- lists all cities in a database
-- db passed in as arg, only use one select
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY id ASC
