CREATE TABLE movies (
    name VARCHAR(255) NOT NULL,
    Release_date SMALLINT NOT NULL,
    Rating FLOAT NOT NULL
);

COPY movies
FROM '/Users/danielraz/Downloads/IMDB Top 250 Movies.csv' delimiter ',' csv header;