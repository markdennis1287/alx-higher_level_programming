-- Create the database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant usage and SELECT privilege to user_0d_2 on hbtn_0d_2 database
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
