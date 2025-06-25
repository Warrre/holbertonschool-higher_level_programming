-- that lists all records of the table
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
