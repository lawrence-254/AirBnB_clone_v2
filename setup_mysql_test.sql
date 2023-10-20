-- a script that prepares a MySQL server for the project
-- create database if does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user if they do not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- give privilages
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
