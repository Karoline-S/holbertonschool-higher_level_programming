-- creates a table
-- db passed in as arg, table: id_not_null
CREATE TABLE IF NOT EXISTS id_not_null
(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
