-- list from two tables
-- second line
SELECT cities.id, cities.name, states.name FROM cities
	WHERE states.name=(SELECT states.name WHERE state_id=cities.id);
