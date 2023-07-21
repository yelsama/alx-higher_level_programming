-- list from two tables
SELECT cities.id cities.name states.name WHERE states.name=(SELECT states.name WHERE state_id=cities.id);