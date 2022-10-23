CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    name TEXT,
    release INT,
    director TEXT,
    genre TEXT
);

CREATE TABLE genres(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE watchlists(
    user_id INT,
    movie_id INT
);

INSERT INTO genres (name) VALUES
('Action'),
('Drama'),
('Horror'),
('Romance'),
('Mystery'),
('Fantasy'),
('Thriller');