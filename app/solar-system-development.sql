CREATE DATABASE solar_system_development;

CREATE TABLE planet (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    planet_name VARCHAR(100),
    description TEXT
);

INSERT INTO planet (planet_name, description)
VALUES ('pluto','used to be a planet but is now mickey mouses dog')
;

