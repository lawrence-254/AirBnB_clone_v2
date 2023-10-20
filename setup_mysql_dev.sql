-- a script that prepares a MySQL server for the project
-- create database if does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--use the created database
USE hbnb_dev_db;
-- create user if they do not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- give privilages
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
