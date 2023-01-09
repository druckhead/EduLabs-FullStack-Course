CREATE DATABASE movies;

DROP DATABASE movies1;

CREATE TABLE movies (
	id serial PRIMARY KEY,
	movie_name varchar(256) NOT NULL,
	release_year smallint NOT NULL,
	imdb_rating float
);

INSERT INTO movies (movie_name, release_year, imdb_rating)
VALUES('The Godfather', 1972, 9.2);

SELECT *
FROM movies;

INSERT INTO movies (movie_name, release_year)
VALUES('The Shawshank Redemption', 1994);

-- CRUD
UPDATE movies
SET imdb_rating = 9.3;

UPDATE movies
SET imdb_rating = 9.2
WHERE id = 1;

INSERT INTO movies (movie_name, release_year)
VALUES ('The Green Mile', 34.5);

DELETE FROM movies
WHERE id = 4;

CREATE TABLE directors (
	id serial PRIMARY KEY,
	director_name varchar(256) NOT NULL,
	origin_country varchar(128)
);

INSERT INTO directors (director_name, origin_country)
VALUES('Francis Ford Coppola', 'Italy');

INSERT INTO directors (director_name)
VALUES('Frank Darabont');

SELECT *
FROM directors d;

ALTER TABLE movies
ADD director_id int;

SELECT *
FROM movies m;

ALTER TABLE movies
ADD CONSTRAINT fk_director_id FOREIGN KEY (director_id) REFERENCES directors(id);

SELECT *
FROM directors d;

SELECT *
FROM movies m;

UPDATE movies
SET director_id = 2
WHERE id = 1;

ALTER TABLE movies
ALTER COLUMN director_id
SET NOT NULL;

INSERT INTO directors (director_name, origin_country)
VALUES('Quentin Tarantino', 'Israel');

INSERT INTO movies (movie_name, release_year, director_id)
VALUES ('Pulp fiction', 1994, 3);

INSERT INTO movies (movie_name, release_year, director_id)
VALUES ('Django Unchained', 2012, 3);

SELECT *
FROM movies
	CROSS JOIN directors;

SELECT *
FROM movies
	JOIN directors ON movies.director_id = directors.id;

--select * from movies
--join directors on movies.director_id > directors.id;
SELECT movie_name,
	release_year,
	director_name
FROM movies m
	JOIN directors d ON m.director_id = d.id;

SELECT movie_name,
	release_year,
	director_name
FROM movies m
	LEFT JOIN directors d ON m.director_id = d.id;

SELECT movie_name,
	release_year,
	director_name
FROM movies m
	RIGHT JOIN directors d ON m.director_id = d.id;

SELECT movie_name,
	release_year,
	director_name
FROM movies m
	FULL OUTER JOIN directors d ON m.director_id = d.id;

SELECT *
FROM movies m;

SELECT director_name,
	COUNT(*)
FROM movies m
	JOIN directors d ON m.director_id = d.id
GROUP BY director_id,
	director_name;