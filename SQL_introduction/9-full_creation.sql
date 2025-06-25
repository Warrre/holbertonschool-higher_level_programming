-- that creates a table second_table in the database
-- hbtn_0c_0 and add multiples rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(10, 'War', 100),
(20, 'Goku', 30),
(30, 'Luffy', 140),
(40, 'Asta', 80);
