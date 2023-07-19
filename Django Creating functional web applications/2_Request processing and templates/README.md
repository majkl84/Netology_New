 * <b>[Ссылка на код занятия](https://github.com/netology-code/DJ_code/tree/master/intro)</b>
 * <b>Работа с конфигом Django</b><br>
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

* <b>Конвертеры маршрутов в Django</b><br>
    Конвертеры маршрутов в Django существуют не для всех типов данных.<br>
    Стандартные конвертеры описаны в документации: (https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters).<br>
    Django помимо стандартных конвертеров предоставляет возможность создать свой конвертер и описать правила конвертации так, как угодно.<br>
    Для этого надо сделать два шага:<br>
    Описать класс конвертера.<br>
    Зарегистрировать конвертер.<br>

    Класс конвертера — это класс с определённым набором атрибутов и методов, описанных в документации (на мой взгляд, несколько странно, что разработчики не сделали базовый абстрактный класс). Сами требования:<br>

    Должен быть атрибут regex, описывающий регулярное выражение для быстрого поиска требуемой подпоследовательности. Чуть позже покажу, как он используется.<br>
    Реализовать метод def to_python(self, value: str) для конвертации из строки (ведь передаваемый маршрут — это всегда строка) в объект python, который в итоге будет передаваться в обработчик.<br>
    Реализовать метод def to_url(self, value) -> str для обратной конвертации из объекта python в строку (используется, когда вызываем django.urls.reverse или тег url).<br>
    Класс для конвертации даты будет выглядеть так:<br>

    class DateConverter:<br>
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'<br>

    def to_python(self, value: str) -> datetime:<br>
        return datetime.strptime(value, '%Y-%m-%d')<br>

    def to_url(self, value: datetime) -> str:<br>
        return value.strftime('%Y-%m-%d')<br>
    Вынесем формат даты в атрибут для упрощения поддержки конвертера:<br>

    class DateConverter:<br>
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'<br>
    format = '%Y-%m-%d'<br>

    def to_python(self, value: str) -> datetime:<br>
        return datetime.strptime(value, self.format)<br>

    def to_url(self, value: datetime) -> str:<br>
        return value.strftime(self.format)<br>
    По итогу описания класса можно зарегистрировать его как конвертер. Для этого в функции register_converter надо указать описанный класс и название конвертера, чтобы использовать его в маршрутах.<br>

    from django.urls import register_converter<br>
    register_converter(DateConverter, 'date')<br>
    Опишем маршруты в urls.py:<br>

    path('users/<int:id>/reports/<date:dt>/', user_report, name='user_report'),<br>
    path('teams/<int:id>/reports/<date:dt>/', team_report, name='team_report'),<br>
    Теперь гарантируется, что обработчики вызываются только в том случае, если конвертер отработает корректно, а это значит, что в обработчик придут параметры нужного типа:<br>

    def user_report(request, id: int, dt: datetime):<br>
    больше никакой валидации в обработчиках<br>
    сразу правильные типы и никак иначе<br>
    