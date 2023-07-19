##### Вебинар №1
* [Знакомство с Django. Подготовка и запуск проекта](https://github.com/majkl84/Netology_new/tree/main/Python%20Getting%20to%20know%20the%20console)
* Introduction to Django. Project preparation and launch
#### Вебинар №2
* [Обработка запросов и шаблоны](https://github.com/majkl84/Netology_new/tree/main/Conditional%20constructions%20-%20Comparison%20operations)
* Request processing and templates
#### Вебинар №3
* [Работа с ORM](https://github.com/majkl84/Netology_new/tree/main/Introduction%20to%20Data%20Types%20and%20Loops)
* Working with ORM
#### Вебинар №4
* [Работа с ORM (2 часть)](https://github.com/majkl84/Netology_new/tree/main/Collections%20of%20data%20-%20Dictionaries%20-%20Sets)
* Working with ORM (Part 2)
#### Вебинар №5
* [Знакомство с API на примере Django REST framework](https://github.com/majkl84/Netology_new/tree/main/Functions%20—%20using%20built-in%20and%20creating%20your%20own)
* Getting to know the API using the Django REST framework example
#### Вебинар №6
* [CRUD в DRF](https://github.com/majkl84/Netology_new/tree/main/OOP%20objects%20and%20classes%20-%20Interaction%20between%20them)
* CRUD в DRF
#### Вебинар №7
* [Разделение доступа в DRF](https://github.com/majkl84/Netology_new/tree/main/OOP%20Inheritance%2C%20encapsulation%20and%20polymorphism)
* Sharing access in DRF
#### Вебинар №8
* [Тестирование Django-приложений с использованием Pytest](https://github.com/majkl84/Netology_new/tree/main/Opening%20and%20reading%20a%20file%2C%20writing%20to%20a%20file)
* Testing Django applications using Py test


* Клиент:
Программа, которая хочет получить информацию.
Физическое устройство, на котором работает программа-клиент.

* Сервер:
Специальная программа, которая даёт информацию.
Физическое устройство, на котором запущена программа-сервер.
Обычно эти программы расположены на разных вычислительных машинах и взаимодействуют между собой по различным протоколам, но они могут располагаться и на одной машине.
Веб-приложение реализует клиент-серверное взаимодействие. Пользователи шлют запросы к серверу, он выдаёт им результат в специальном виде html- или JSON-данных.
Django-проект выступает в роли сервера. Чтобы запустить проект, выполните команды:
1 $ ./manage.py runserver # запускает проект
Классическим клиентом для веб-сервера является браузер, например Google Chrome, в нем можно указать адрес и порт сервера (по умолчанию для Django - http://127.0.0.1:8000), тогда браузер (клиент) начнет взаимодействие с Django (сервером).

* MVC и Django
Django генерирует структуру проекта самостоятельно. Благодаря этому даже новые разработчики знают, где и что можно искать.
При разработке Django-приложений очень важно придерживаться соглашений.
Проекты на Django должны придерживаться паттерна MVC: model-view-controller
— модель-представление-контроллёр.

Управление логикой при ответе -> view;
Как будет выглядеть страница -> template;
Состояние приложения -> model.

* [Дополнительный материал](https://docs.djangoproject.com/en/3.2/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)
Правило: не мешать всё в одну кучу.