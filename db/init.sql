CREATE DATABASE sourcesagedb;
CREATE USER 'sourcesageuser'@'%' IDENTIFIED BY 'password!';
GRANT ALL PRIVILEGES ON sourcesagedb.* TO 'sourcesageuser'@'%' IDENTIFIED BY 'password!';
