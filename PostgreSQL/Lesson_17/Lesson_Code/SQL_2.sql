CREATE TABLE public.directors (
  id serial PRIMARY KEY,
  name varchar(256) NOT NULL
);

CREATE TABLE public.movies (
  id serial PRIMARY KEY,
  name varchar(256) NOT NULL,
  YEAR int NOT NULL,
  director_id int NOT NULL,
  CONSTRAINT fk_director FOREIGN KEY(director_id) REFERENCES directors(id)
);

INSERT INTO directors(name)
VALUES ('Frank Darabont');

INSERT INTO directors(name)
VALUES ('Francis Ford Coppola');

INSERT INTO directors(name)
VALUES ('Steven Spielberg');

INSERT INTO directors(name)
VALUES ('Quentin Tarantino');

INSERT INTO movies ("id", "name", "year", director_id)
VALUES(1, 'The Godfather', 1972, 2);

INSERT INTO movies ("id", "name", "year", director_id)
VALUES(2, 'The Shawshank Redemption', 1994, 1);

INSERT INTO movies (id, name, YEAR, director_id)
VALUES (3, 'The Green Mile', 1999, 1);

INSERT INTO movies (id, name, YEAR, director_id)
VALUES (4, 'The Mist', 2007, 1);

INSERT INTO movies (id, name, YEAR, director_id)
VALUES (5, 'Dracula', 1992, 2);

INSERT INTO movies (id, name, YEAR, director_id)
VALUES (6, 'Gardens of stone', 1987, 2);

INSERT INTO movies (id, name, YEAR, director_id)
VALUES (7, 'Pulp fiction', 1994, 4);

ALTER TABLE movies
ADD length_in_min float;

UPDATE movies
SET length_in_min = 175
WHERE id = 1;

UPDATE movies
SET length_in_min = 142
WHERE id = 2;

UPDATE movies
SET length_in_min = 189
WHERE id = 3;

UPDATE movies
SET length_in_min = 126
WHERE id = 4;

UPDATE movies
SET length_in_min = 128
WHERE id = 5;

UPDATE movies
SET length_in_min = 111
WHERE id = 6;

UPDATE movies
SET length_in_min = 154
WHERE id = 7;

CREATE TABLE public.series (
  id serial PRIMARY KEY,
  name varchar(256) NOT NULL
);

ALTER TABLE movies
ADD series_id int;

ALTER TABLE movies
ADD CONSTRAINT fk_series FOREIGN KEY(series_id) REFERENCES series(id);

INSERT INTO series(name)
VALUES ('The Godfather');

INSERT INTO series(name)
VALUES ('Avatar');

INSERT INTO movies (id, name, YEAR, director_id)
VALUES (8, 'The Godfather: Part II', 1974, 2);

INSERT INTO movies (id, name, YEAR, director_id)
VALUES (9, 'The Godfather: Part III', 1990, 2);

UPDATE movies
SET length_in_min = 202
WHERE id = 8;

UPDATE movies
SET length_in_min = 142
WHERE id = 9;

INSERT INTO directors(name)
VALUES ('James Cameron');

INSERT INTO movies(id, name, YEAR, director_id)
VALUES(11, 'Avatar', 2009, 5);

UPDATE movies
SET length_in_min = 142
WHERE id = 11;

INSERT INTO movies(id, name, YEAR, director_id)
VALUES(10, 'Avatar: The Way of Water', 2022, 5);

UPDATE movies
SET length_in_min = 192
WHERE id = 10;

UPDATE movies
SET series_id = 1
WHERE id = 1;

UPDATE movies
SET series_id = 1
WHERE id = 8;

UPDATE movies
SET series_id = 1
WHERE id = 9;

UPDATE movies
SET series_id = 2
WHERE id = 11;

UPDATE movies
SET series_id = 2
WHERE id = 10;

-- QUERIES
-- a
SELECT m.id,
  m.name,
  m.year,
  m.length_in_min,
  d.name
FROM movies m
  JOIN directors d ON m.director_id = d.id;

-- b
SELECT s.name,
  COUNT(*) AS movies_in_series
FROM movies m
  JOIN series s ON m.series_id = s.id
GROUP BY s.name;

-- c
SELECT d.name,
  COUNT(*) AS movies_by_director
FROM movies m
  JOIN directors d ON m.director_id = d.id
GROUP BY d.name;

-- d
SELECT d.name,
  COUNT(*) AS movies_by_director,
  COUNT(DISTINCT(s.id)) AS series_by_director
FROM movies m
  JOIN directors d ON m.director_id = d.id
  JOIN series s ON m.series_id = s.id
GROUP BY d.name,
  s.id;

-- e
SELECT DISTINCT m.name AS movie_name,
  d.name AS director_name,
  s.name AS series_name
FROM movies m
  JOIN directors d ON d.id = m.director_id
  JOIN series s ON s.id = m.series_id
WHERE m.series_id IN (
    SELECT m.series_id
    FROM movies m
    GROUP BY m.series_id
    HAVING COUNT(m.series_id) >= 2
  );

-- f
SELECT m.name,
  m.year,
  m.length_in_min,
  d.name AS director_name
FROM movies m
  JOIN directors d ON d.id = m.director_id
WHERE m.series_id IS NULL;