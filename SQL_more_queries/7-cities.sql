CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL UNIQUE AUTO_INCREMENT,
    state_id INT,
    name VARCHAR(256),
    PRIMARY KEY ('id'),
    FOREIGN KEY ('state_id') REFERENCES states ('id')
);