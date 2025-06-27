-- that creates the database
-- hbtn_0d_usa and the table states
CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
CREATE TABLE if NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
