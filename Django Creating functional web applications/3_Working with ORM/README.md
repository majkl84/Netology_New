[Ссылка на код занятия](https://github.com/netology-code/DJ_code/tree/master/orm)
* **Базы данных**<br>
**Для чего нужна база данных:**<br>
* хранение данных,
* обработка данных,
* управление данными,
* совместная работа нескольких пользователей.
У стандартных файлов есть ряд недостатков по сравнению с базой данных:<br>

1. При хранении в файле нужно самостоятельно писать проверки структуры.<br>
2. Возможна потеря данных в случае ошибок.<br>
3. С файлом сложно работать нескольким людям.<br>
4. Для работы с большим объёмом данных нужны высокоэффективные алгоритмы:<br>
    * поиск нужного элемента в файле,
    * получение связанных данных из разных файлов,
    * сортировка данных.

**СУБД** представляет собой совокупность формата хранения и кода для работы с данными, однако для разработчика СУБД — сочетание драйвера и языковых запросов SQL.
Популярные СУБД:<br>

* MySQL,
* PostgreSQL,
* SQLite,
* Oracle и другие.<br>

**Таблица (база данных)** — это совокупность связанных данных, хранящихся в структурированном виде. Таблица состоит **из столбцов и строк,** где строки называются записью (кортежем), а столбцы — атрибутами или полями (доменами).<br>

ID      | brand | name  | color
:------:|:-----:|:-----:|:-----:
1       | Ford  | Focus | red
2       | Lada  | Kalina| purple

**Поле**, каждое значение которого однозначно определяет соответствующую запись, называется **простым ключом** или **primary key (ключевым полем).** В этом случае это поле **id.**

**SQL** — язык работы с данными:


1 -- запрашиваем разные сущности, хранящиеся в отдельных таблицах<br>
2<br>
3 SELECT name, birthday, gender FROM person;<br>
4  <br>
5 SELECT brand, name, color FROM car;<br><br>
Можно и из связанных данных получать общую картину:<br>

1 -- у кого какая машина<br>
2 SELECT person.name, car.brand, car.name<br>
3  FROM person INNER JOIN car ON car.id = person.car_id<br>

**Связь** позволяет **моделировать** отношения между объектами. Существует **4 типа связей:**

1. **Один к одному** — любому экземпляру сущности А соответствует только один экземпляр сущности В и наоборот. Этот тип связи редко используется. Например, для расширения таблицы.
2. **Один ко многим** — любому экземпляру сущности А соответствует 0, 1 или несколько экземпляров сущности В, но любому экземпляру сущности В соответствует только один экземпляр сущности А. Например: один учитель — много учеников.
3. **Многие к одному** — любому экземпляру сущности А соответствует только один экземпляр сущности В, но любому экземпляру сущности В соответствует 0, 1 или несколько экземпляров сущности А. Например: много учителей — один ученик.
4. **Многие ко многим** — любому экземпляру сущности А соответствует 0, 1 или несколько экземпляров сущности В, и любому экземпляру сущности В соответствует 0, 1 или несколько экземпляров сущности А. Например: множество учеников — множество учителей.

**Модели в Django**<br>
В Django ORM реализовано множество типов данных для атрибутов моделей:
https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types

Чтобы выбрать правильный тип для атрибута, необходимо проанализировать поставленную задачу и определить тип по допустимым значениям.

Так как модель это Python класс, то в модели, помимо описания атрибутов, можно реализовывать методы и свойства.

Например, можно реализовать магический метод str, чтобы получить желаемое отображение объекта при выводе на экран:

1. class Car(models.Model):
2.    …
3. 
4.    def __str__(self):
5.        return f'{self.brand}, {self.model}: {self.color}'