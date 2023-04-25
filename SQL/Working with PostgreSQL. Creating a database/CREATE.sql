CREATE TABLE genres (
    id INT CONSTRAINT genre_pk PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE artists (
    id INT CONSTRAINT artist_pk PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE albums (
    id INT CONSTRAINT album_pk PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_date DATE,
    total_length TIME,
    label VARCHAR(255),
    is_compilation BOOLEAN
);

CREATE TABLE tracks (
    id INT CONSTRAINT track_pk PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    length TIME,
    album_id INT CONSTRAINT track_album_fk REFERENCES albums(id) ON DELETE CASCADE
);

CREATE TABLE compilations (
    id INT CONSTRAINT compilation_pk PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year INT
);

CREATE TABLE artist_genre (
    artist_id INT CONSTRAINT artist_genre_artist_fk REFERENCES artists(id) ON DELETE CASCADE,
    genre_id INT CONSTRAINT artist_genre_genre_fk REFERENCES genres(id) ON DELETE CASCADE,
    CONSTRAINT artist_genre_pk PRIMARY KEY (artist_id, genre_id)
);

CREATE TABLE album_artist (
    album_id INT CONSTRAINT album_artist_album_fk REFERENCES albums(id) ON DELETE CASCADE,
    artist_id INT CONSTRAINT album_artist_artist_fk REFERENCES artists(id) ON DELETE CASCADE,
    CONSTRAINT album_artist_pk PRIMARY KEY (album_id, artist_id)
);

CREATE TABLE compilation_track (
    compilation_id INT CONSTRAINT compilation_track_compilation_fk REFERENCES compilations(id) ON DELETE CASCADE,
    track_id INT CONSTRAINT compilation_track_track_fk REFERENCES tracks(id) ON DELETE CASCADE,
    CONSTRAINT compilation_track_pk PRIMARY KEY (compilation_id, track_id)
);