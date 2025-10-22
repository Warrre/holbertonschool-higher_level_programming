-- This script creates the database hbtn_0d_usa and the table states
-- The table states has an auto-incremented unique id (primary key, not null)
-- and a name (VARCHAR(256), not null)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
