-- convert database, table and field to UTF8
-- db: hbtn_0c_0, table: first_table, field: name (first_table)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
