--Количество исполнителей в каждом жанре:
SELECT genres.name, COUNT(DISTINCT artists.id) AS artist_count
FROM genres
LEFT JOIN artist_genre ON genres.id = artist_genre.genre_id
LEFT JOIN artists ON artist_genre.artist_id = artists.id
GROUP BY genres.id;
--Количество треков, вошедших в альбомы 1990-2000 годов:
SELECT COUNT(tracks.id) AS track_count
FROM tracks
JOIN albums ON tracks.album_id = albums.id
WHERE release_date BETWEEN '1990-01-01' AND '2000-12-31';
--Средняя продолжительность треков по каждому альбому:
SELECT albums.title, AVG(EXTRACT(EPOCH FROM tracks.length)) AS avg_track_length
FROM albums
JOIN tracks ON albums.id = tracks.album_id
GROUP BY albums.id, albums.title;
--Все исполнители, которые не выпустили альбомы в 1990 году:
SELECT artists.name
FROM artists
LEFT JOIN album_artist ON artists.id = album_artist.artist_id
LEFT JOIN albums ON album_artist.album_id = albums.id
WHERE albums.release_date NOT BETWEEN '1990-01-01' AND '1990-12-31' OR albums.release_date IS NULL;
--Названия сборников, в которых присутствует конкретный исполнитель:
SELECT compilations.title
FROM compilations
JOIN compilation_track ON compilations.id = compilation_track.compilation_id
JOIN tracks ON compilation_track.track_id = tracks.id
JOIN album_artist ON tracks.album_id = album_artist.album_id
JOIN artists ON album_artist.artist_id = artists.id
WHERE artists.name = 'Queen';
--Название альбомов, в которых присутствуют исполнители более 1 жанра:
SELECT DISTINCT albums.title
FROM albums
JOIN album_artist ON albums.id = album_artist.album_id
JOIN artists ON album_artist.artist_id = artists.id
JOIN artist_genre ON artists.id = artist_genre.artist_id
GROUP BY albums.id, artist_genre.artist_id
HAVING COUNT(DISTINCT artist_genre.genre_id) > 1;
--Наименование треков, которые не входят в сборники:
SELECT tracks.title
FROM tracks
LEFT JOIN compilation_track ON tracks.id = compilation_track.track_id
WHERE compilation_track.compilation_id IS NULL;
--Исполнитель(-ей), написавшего самый короткий по продолжительности трек:
SELECT artists.name
FROM tracks
JOIN albums ON tracks.album_id = albums.id
JOIN album_artist ON albums.id = album_artist.album_id
JOIN artists ON album_artist.artist_id = artists.id
WHERE tracks.length = (SELECT MIN(length) FROM tracks);
--Название альбомов, содержащих наименьшее количество треков:
SELECT albums.title
FROM albums
JOIN tracks ON albums.id = tracks.album_id
GROUP BY albums.id
HAVING COUNT() = (
SELECT MIN(track_count)
FROM (SELECT album_id, COUNT() AS track_count
FROM tracks
GROUP BY album_id) AS track_counts
);
