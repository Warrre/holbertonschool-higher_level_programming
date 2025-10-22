-- This script creates the database hbtn_0d_usa and the table cities.
SELECT cities.id, cities.name, states.name FROM cities 
INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC ;
