CREATE DATABASE sourcesagedb;
CREATE USER 'sourcesageuser'@'localhost' IDENTIFIED BY 'password!';
GRANT ALL PRIVILEGES ON sourcesagedb.* TO 'sourcesageuser'@'locahost' IDENTIFIED BY 'password!';
