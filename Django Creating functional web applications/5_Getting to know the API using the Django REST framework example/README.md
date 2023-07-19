[Ссылка на код к занятию](https://github.com/netology-code/DJ_code/tree/master/api)

**REST API** — архитектурный стиль проектирования API.

**Основные требования:**

* взаимодействие клиент-сервер;
* запросы содержат в себе все необходимое состояние;
* строгое именование ресурсов;
* использование семантики HTTP-методов и определенных кодов возврата.

![Как_именуются_ресурсы!](https://github.com/majkl84/Netology_new/blob/main/Django%20Creating%20functional%20web%20applications/5_Getting%20to%20know%20the%20API%20using%20the%20Django%20REST%20framework%20example/How-are-the-resources-named.png)

**Generic APIView классы**

В DRF реализованы основные классы для работы с данными, такие как ListAPIView, RetrieveAPIView и т.п. Подробнее про такие классы и их возможности можно почитать на этом ресурсе:
https://www.django-rest-framework.org/api-guide/generic-views/