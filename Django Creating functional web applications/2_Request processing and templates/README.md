 [Ссылка на код занятия](https://github.com/netology-code/DJ_code/tree/master/intro)

 **Работа с конфигом Django**

 Конфигурация Django задается в файле settings.py, который можно найти в главном пакете проекта. В этом файле уже описано множество переменных, на которые Django опирается при работе.<br>

Дополнительная информация про конфигурацию Django: (https://docs.djangoproject.com/en/3.2/topics/settings/)<br>
В settings.py можно добавлять свои собственные переменные и потом пользоваться ими в любом удобном месте.<br>
Для получения значений из конфигурации, необходимо обращаться к полям в объекте settings:

    # именно так надо импортировать настройки
    from django.conf import settings
    from django.http import HttpResponse

    def hello_view(request): 
    msg = f'Свяжитесь с админом {settings.CONTANCT_EMAIL}' 
    return HttpResponse('Всем привет! Я Django! ' + msg)

**Конвертеры маршрутов в Django**

Конвертеры маршрутов в Django существуют не для всех типов данных.

Стандартные конвертеры описаны в документации: (https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters).

Django помимо стандартных конвертеров предоставляет возможность создать свой конвертер и описать правила конвертации так, как угодно.

Для этого надо сделать два шага:<br>
Описать класс конвертера.<br>
Зарегистрировать конвертер.<br>

Класс конвертера — это класс с определённым набором атрибутов и методов, описанных в документации (на мой взгляд, несколько странно, что разработчики не сделали базовый абстрактный класс). Сами требования:

1. Должен быть атрибут **regex**, описывающий регулярное выражение для быстрого поиска требуемой подпоследовательности. Чуть позже покажу, как он используется.<br>
2. Реализовать метод **def to_python(self, value: str)** для конвертации из строки (ведь передаваемый маршрут — это всегда строка) в объект python, который в итоге будет передаваться в обработчик.<br>
3. Реализовать метод **def to_url(self, value) -> str** для обратной конвертации из объекта python в строку (используется, когда вызываем **django.urls.reverse или тег url)**.

Класс для конвертации даты будет выглядеть так:

1. class DateConverter:
2.    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
3. 
4.    def to_python(self, value: str) -> datetime:
5.        return datetime.strptime(value, '%Y-%m-%d')
6. 
7.    def to_url(self, value: datetime) -> str:
8.          return value.strftime('%Y-%m-%d')

Вынесем формат даты в атрибут для упрощения поддержки конвертера:

1. class DateConverter:
2.    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
3.    format = '%Y-%m-%d'>
4. 
5.    def to_python(self, value: str) -> datetime:
6.        return datetime.strptime(value, self.format)
7. 
8.    def to_url(self, value: datetime) -> str:
9.        return value.strftime(self.format)

По итогу описания класса можно зарегистрировать его как конвертер. Для этого в функции **register_converter** надо указать описанный класс и название конвертера, чтобы использовать его в маршрутах.

1. from django.urls import register_converter
2.    register_converter(DateConverter, 'date')
3.    

Опишем маршруты в urls.py:

1. path('users/<int:id>/reports/<date:dt>/', user_report, name='user_report'),
2. path('teams/<int:id>/reports/<date:dt>/', team_report, name='team_report'),

Теперь гарантируется, что обработчики вызываются только в том случае, если конвертер отработает корректно, а это значит, что в обработчик придут параметры нужного типа:

1. def user_report(request, id: int, dt: datetime):
2.    больше никакой валидации в обработчиках
3.    сразу правильные типы и никак иначе
    