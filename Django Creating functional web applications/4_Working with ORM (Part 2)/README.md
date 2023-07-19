[Ссылка на код к занятию](https://github.com/netology-code/DJ_code/tree/master/orm_advanced)

**Many-to-many с помощью through**

Когда мы избавились от дублирования информации, удалив свойство products из модели Order, мы лишились возможности напрямую получать доступ к продуктам в заказе.

Косвенно можно получить продукты в заказе так:

1. order_positions = some_order.positions.all()
2. order_products = {pos.product for pos in order_positions}

Однако такой метод предполагает, что во всех местах, где нам потребуется получить продукты из заказа, придётся писать одинаковый код, что не всегда удобно. Также и в обратную сторону: чтобы найти все заказы, в которых участвует продукт, необходимо написать такой код:

1. product_positions = some_product.positions.all()
2. product_orders = {pos.order for pos in product_positions}

А ведь в первоначальном варианте, когда Django автоматически создавал связь m2m, было удобнее — было свойство products в классе Order и related_name orders.
На самом деле такую связь можно оставить, просто надо явно указать, что связь будет осуществляться через специальную модель. Тогда Django не будет создавать автоматическую связь m2m, но при этом останутся необходимые свойства:

1. class Order(models.Model):
2.    products = models.ManyToManyField(Product, related_name='orders', through='OrderPosition')

Теперь можно получать продукты из заказа простым способом:<br>
<span style="color:pink">order_products = some_order.products.all()

Аналогично с заказами, в которых участвует продукт:<br>
<span style="color:pink">product_orders = some_product.orders.all()

**Django Debug Toolbar**
Для удобного мониторинга и отладки проекта можно установить специальную библиотеку - Django Debug Toolbar.

Полное руководство по библиотеке: django-debug-toolbar.readthedocs.io...index.html

Чтобы запустить Django Debug Toolbar необходимо выполнить несколько действий:
установить библиотеку:
pip install django-debug-toolbar

Настроить переменную INSTALLED_APPS в settings.py: убедиться, что присутствует приложение django.contrib.staticfiles и добавить новое приложение debug_toolbar (обязательно добавить его после django.contrib.staticfiles):

1. INSTALLED_APPS = [
2.    # ...
3.    'django.contrib.staticfiles',
4.    # ...
5.    'debug_toolbar',
6. ]

Настроить переменную STATIC_URL в settings.py:
STATIC_URL = '/static/'

Убедиться, что в переменной TEMPLATES в settings.py параметр APP_DIRS установлен в значение True

Добавить в переменную MIDDLEWARE в settings.py в самое начало:

1. MIDDLEWARE = [
2.    'debug_toolbar.middleware.DebugToolbarMiddleware',
3.    # ...
4. ]

Добавить переменную INTERNAL_IPS в settings.py:

1. INTERNAL_IPS = [
2.    '127.0.0.1',
3. ]

Добавить маршрут в самый конец urlpatterns в файле urls.py:

1. import debug_toolbar
2. from django.conf import settings
3. from django.urls import include, path
4. 
5. urlpatterns = [
6.     ...
7.    path('__debug__/', include(debug_toolbar.urls)),
8. ]

После выполнения всех действий при ответе сервера в браузере справа будет доступен инструмент Django Debug Toolbar.

[Пример настроенного проекта](https://github.com/jazzband/django-debug-toolbar/tree/main/example)