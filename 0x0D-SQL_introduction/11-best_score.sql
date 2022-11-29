-- lists all records (name and score only) of the table second_table sorted by score
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
