-- This script converts hbtn_0c_0 database to UTF8
-- convert database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_unicode_ci;
-- convert table
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
-- convert name column in table
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci;
