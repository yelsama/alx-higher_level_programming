-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
FROM cities SELECT id, name WHERE state_id=(FROM states SELECT id WHERE name='Clifornia');
