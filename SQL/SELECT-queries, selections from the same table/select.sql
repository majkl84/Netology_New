--Название и год выхода альбомов, вышедших в 1984 году:
SELECT title, release_date FROM albums
WHERE release_date >= '1984-01-01' AND release_date <= '1984-12-31';
--Название и продолжительность самого длительного трека:
SELECT title, length FROM tracks
WHERE length = (SELECT MAX(length) FROM tracks);
--Название треков, продолжительность которых не менее 3,5 минуты:
SELECT title FROM tracks
WHERE length >= '00:03:30';
--Названия сборников, вышедших в период с 1990 по 2000 год включительно:
SELECT title FROM compilations
WHERE release_year >= 1990 AND release_year <= 2000;
--Исполнители, чье имя состоит из 1 слова:
SELECT name FROM artists
WHERE name NOT LIKE '% %';
--Например, необходимо найти все треки, в которых есть слово by
SELECT title FROM tracks
WHERE string_to_array(lower(title), ' ') && array['by'];