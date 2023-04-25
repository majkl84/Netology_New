######## Task_1###################
# geo_logs = [
#     {'Visit1': ['Москва', 'Россия']},
#     {'Visit2': ['Дели', 'Индия']},
#     {'Visit3': ['Владимер', 'Россия']},
#     {'Visit4': ['Лиссабон', 'Португаляи']},
#     {'Visit5': ['Париж', 'Франция']},
#     {'Visit6': ['Лиссабон', 'Португаляи']},
#     {'Visit7': ['Тула', 'Россия']},
#     {'Visit8': ['Тула', 'Россия']},
#     {'Visit9': ['Курск', 'Россия']},
#     {'Visit10': ['Архангельск', 'Россия']}
# ]
# lists = []
# for dict_ in geo_logs:
#     for list_item in list(dict_.values()):
#         for n in range(len(list_item)):
#             if list_item[n] == 'Россия':
#                 # lists.append(list_item)
#                 lists.append(dict_)
# print(lists)

######## Task_2###################
# ids = {'user1': [213, 213, 213, 15, 213],
#         'user2':[54, 54, 119, 119, 119],
#         'user3': [213, 98, 98, 35]}
# ######## Вариант-1 ###############
# ids_1 = set(ids.get('user1'))
# ids_2 = set(ids.get('user2'))
# ids_3 = set(ids.get('user3'))
# unique_ids = ids_1 | ids_2 | ids_3
# print(list(unique_ids))
######## Вариант-2 ###############

# number = set()
# for i in ids.values():
#     for j in i:
#         number.add(j)
# print(list(number))

######## Task_3###################
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'афиша',
    'кино',
    'как изучить язык програмирования Python'

]
requests = {}
percent = int(100 / (len(queries)))
for k in queries:
    req = len(k.split())
    requests[req] = requests.get(req, 0) + 1

for words_number, requests_number in sorted(requests.items()):
    print(
        f' "Количество запросов из" {words_number} " слов(а) составляет" {round((requests_number * percent), 2)} "процентов"')

######## Task_4###################
# stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
# m = stats.values()
# i = max(m)
# for name, value in stats.items():
#       if value == i:
#           print(name)
