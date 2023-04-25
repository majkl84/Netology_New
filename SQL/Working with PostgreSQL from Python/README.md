### Как установить DBeaver
В данной инструкции информация по скачиванию и установке DBeaver.

DBeaver - это клиент SQL и средство администрирования базы данных. Он предоставляет редактор, поддерживающий компиляцию кода и подсветку синтаксиса, архитектуру плагинов (основанную на архитектуре плагинов Eclipse), которая позволяет модифицировать поведение большой части приложения для обеспечения специальных функций базы данных, которые не зависят от самой базы данных. Приложение, написанно на Java и основанно на платформе Eclipse.

Поддерживаемая операционная система: Windows, Mac, Linux

Лицензия: Apache, бесплатное программное обеспечение с открытым исходным кодом.

Установка
[Перейти по ссылке](https://dbeaver.io/download/) и скачать установщик под свою операционную систему.

Запустить установщик и следовать подсказкам.

#### Первый запуск

* После запуска отменить создание новой Базы Данных
* Выбрать тип нового соединения PostgreSQL и нажать Далее
* В поле аутентификация ввести пароль суперпользователя Базы данных и нажать Готово
  
* [Ограничения в PostgreSQL:](https://www.postgresql.org/docs/current/ddl-constraints.html)
* [Разбор связей между таблицами базы данных с примерами:](https://habr.com/ru/post/488054/)
* [Создание таблиц:](https://www.postgresql.org/docs/12/sql-createtable.html)
* [Типы полей:](https://www.postgresql.org/docs/12/datatype.html)
* [Ограничения:](https://www.postgresql.org/docs/current/ddl-constraints.html)
* 

* Листинги кода к занятию «Работа с SQL. Создание БД»

-- все, что начинается с двух дефисов - это комментарий

-- один к одному (1 вариант)

--CREATE TABLE IF NOT EXISTS Student (
--	email VARCHAR(80) PRIMARY KEY,
--	name VARCHAR(40) NOT NULL,
--	password VARCHAR(128) NOT NULL
--);
--
--CREATE TABLE IF NOT EXISTS StudentInfo (
--	email VARCHAR(80) PRIMARY KEY REFERENCES Student(email),
--	birthday date,
--	city VARCHAR(60),
--	roi TEXT
--);

-- один к одному (2 вариант)

CREATE TABLE IF NOT EXISTS Student (
	id SERIAL PRIMARY KEY,
	email VARCHAR(80) UNIQUE NOT NULL,
	name VARCHAR(40) NOT NULL,
	PASSWORD VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS StudentInfo (
	id INTEGER PRIMARY KEY REFERENCES Student(id),
	birthday date,
	city VARCHAR(60),
	roi TEXT
);

-- один ко многим

CREATE TABLE IF NOT EXISTS Course (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	description TEXT
);

CREATE TABLE IF NOT EXISTS HomeworkTask (
	id SERIAL PRIMARY KEY,
	course_id INTEGER NOT NULL REFERENCES Course(id),
	number INTEGER NOT NULL,
	description TEXT NOT NULL
);

-- многие ко многим (1 вариант)

CREATE TABLE IF NOT EXISTS CourseStudent (
	course_id INTEGER REFERENCES Course(id),
	student_id INTEGER REFERENCES Student(id),
	CONSTRAINT pk PRIMARY KEY (course_id, student_id)
);

-- многие ко многим (2 вариант)

CREATE TABLE IF NOT EXISTS HomeworkSolution (
	id SERIAL PRIMARY KEY,
	task_id INTEGER NOT NULL REFERENCES HomeworkTask(id),
	student_id INTEGER NOT NULL REFERENCES Student(id),
	solution TEXT NOT NULL
);