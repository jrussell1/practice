CREATE DATABASE seinfeld;
USE seinfeld;

-- Created the table "actors" 
CREATE TABLE actors
(
  id int
  AUTO_INCREMENT,
  name VARCHAR (100) NOT NULL,
  coolness_points INT NOT NULL,
  attitude VARCHAR (100) NOT NULL, 
  PRIMARY KEY (id)
);

  -- Inserted a set of records into the table
  INSERT INTO actors (name, coolness_points, attitude)
  VALUES
    ("Jerry", 80, "cool as the other side of the pillow");
  INSERT INTO actors (name, coolness_points, attitude)
  VALUES
    ("George", 40, "neurotic");
  INSERT INTO actors (name, coolness_points, attitude)
  VALUES
    ("Soup Nazi", 99, "napoleon complex");
  INSERT INTO actors (name, coolness_points, attitude)
  VALUES
    ("Elaine", 60, "boss");

