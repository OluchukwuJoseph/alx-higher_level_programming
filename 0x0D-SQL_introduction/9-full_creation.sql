-- This script creates and inserts into second_table
-- create table
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- insert first row in table
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
-- insert second row in table
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
-- insert thrid row in table
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
-- insert fourth row in table
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
