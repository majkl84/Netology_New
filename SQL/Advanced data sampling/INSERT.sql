-- Добавление жанров
INSERT INTO genres (id, name) VALUES 
(1, 'Rock'),
(2, 'Pop'),
(3, 'Hip hop'),
(4, 'Jazz'),
(5, 'Electronic'),
(6, 'Classical'),
(7, 'Country'),
(8, 'Blues');

-- Добавление артистов
INSERT INTO artists (id, name) VALUES 
(1, 'The Beatles'),
(2, 'Queen'),
(3, 'Led Zeppelin'),
(4, 'Michael Jackson'),
(5, 'Madonna'),
(6, 'Eminem'),
(7, 'Coldplay'),
(8, 'AC/DC');

-- Добавление альбомов
INSERT INTO albums (id, title, release_date, total_length, label, is_compilation) VALUES 
(1, 'Abbey Road', '1969-09-26', '00:47:00', 'Apple', false),
(2, 'A Night at the Opera', '1975-11-21', '00:43:13', 'EMI', false),
(3, 'Led Zeppelin IV', '1971-11-08', '00:42:38', 'Atlantic', false),
(4, 'Thriller', '1982-11-30', '00:42:19', 'Epic', false),
(5, 'Like a Virgin', '1984-11-12', '00:37:48', 'Sire', false),
(6, 'The Slim Shady LP', '1999-02-23', '01:00:27', 'Interscope', false),
(7, 'Parachutes', '2000-07-10', '00:41:50', 'Parlophone', false),
(8, 'Highway to Hell', '1979-07-27', '00:41:23', 'Atlantic', false);

-- Добавление треков
INSERT INTO tracks (id, title, length, album_id) VALUES 
(1, 'Come Together', '00:04:20', 1),
(2, 'Bohemian Rhapsody', '00:05:55', 2),
(3, 'Stairway to Heaven', '00:08:02', 3),
(4, 'Billie Jean', '00:04:54', 4),
(5, 'Material Girl', '00:04:00', 5),
(6, 'My Name Is', '00:04:28', 6),
(7, 'Yellow', '00:04:29', 7),
(8, 'Highway to Hell', '00:03:29', 8),
(9, 'Imagine', '00:03:04', 1),
(10, 'Don''t Stop Me Now', '00:03:30', 2),
(11, 'Kashmir', '00:08:29', 3),
(12, 'Beat It', '00:04:18', 4),
(13, 'Like a Virgin', '00:03:10', 5),
(14, 'The Real Slim Shady', '00:04:44', 6),
(15, 'Clocks', '00:05:07', 7),
(16, 'by myself', '00:05:07', 7),
(17, 'order by', '00:05:07', 7),
(18, 'by', '00:05:07', 7),
(19, 'near by window', '00:05:07', 7),
(20, 'byte', '00:05:07', 7);

-- Добавление компиляций
INSERT INTO compilations (id, title, release_year) VALUES 
(1, 'Greatest Hits', 1981),
(2, 'The Immaculate Collection', 1990),
(3, 'The Eminem Show', 2002),
(4, '1', 2000),
(5, 'The Beatles Anthology', 1995),
(6, 'Queen Rocks', 1997),
(7, 'Led Zeppelin Remasters', 1990),
(8, 'The Very Best of AC/DC', 2009);

-- Добавление связей артистов и жанров
INSERT INTO artist_genre (artist_id, genre_id) VALUES 
(1, 1),
(1, 4),
(2, 2),
(2, 5),
(3, 1),
(3, 4),
(4, 3),
(5, 2),
(5, 5),
(6, 3),
(7, 1),
(8, 1),
(8, 8);

-- Добавление связей альбомов и артистов
INSERT INTO album_artist (album_id, artist_id) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8);

-- Добавление связей компиляций и треков
INSERT INTO compilation_track (compilation_id, track_id) VALUES 
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(2, 13),
(3, 6),
(3, 14),
(3, 15),
(4, 1),
(4, 9),
(4, 10),
(5, 1),
(5, 2),
(5, 3),
(6, 2),
(6, 11),
(6, 12),
(7, 3),
(7, 11),
(7, 15),
(8, 8),
(8, 12),
(8, 15);