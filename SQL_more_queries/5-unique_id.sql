-- This script creates the table unique_id with two columns:
-- id (INT, default value 1, must be unique) and name (VARCHAR(256)).
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
