CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    name TEXT,
    release INT,
    director TEXT
);

CREATE TABLE actors(
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INT,
    movieId INT
);

CREATE TABLE genres(
    id SERIAL PRIMARY KEY,
    name TEXT,
    movieId INT
)