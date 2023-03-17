# pupils = ['Иванов', 'Петров', 'Баширов', 'Сидоров']

# print(pupils [0])
# print(pupils [2])

# languages = ['Python', 'C#', 'Java', 'C++']
# pupils = ['Иванов', 'Петров', 'Баширов', 'Сидоров']

# print('Язык программирования', languages[0], 'изучает', pupils[0])

# languages = [('Python', 'Иванов'),
#              ('C#', 'Петров'),
#              ('Java', 'Баширов'),
#              ('C++', 'Сидоров')]

# print('Язык программирования', languages[2][0], 'изучает', languages[2][1])

# languages = [('Python', 'Иванов'),
#              ('C#', 'Петров'),
#              ('Java', 'Баширов'),
#              ('C++', 'Сидоров')]

# for item in languages:
#     if item[0] == 'C++':
#         print('Язык программирования', item[0], 'изучает', item[1])

# Создание словаря

# languages = {'Python': ['Иванов','Петров'],
#              'C#': 'Петров',
#              'Java': 'Баширов',
#              'C++': 'Сидоров'}
# print(languages)

# languages = {'Python': 'Иванов',
#              'C#': 'Петров',
#              'Java': 'Баширов',
#              'C++': 'Сидоров'}

# print('Язык программирования C# изучает', languages['C#'])

# languages = {}
# print(type(languages))


# languages = {'Python': 'Иванов',
#              'C#': 'Петров',
#              'Java': 'Баширов',
#              'C++': 'Сидоров'}

# print('Язык программирования Pascal изучает', languages['Pascal'])
# приводит к возникновению ошибки KeyError.
#  Ошибка KeyError возникнет и при попытке извлечь значение по несуществующему ключу.

# languages = {'Python': 'Иванов',
#              'C#': 'Петров',
#              'Java': 'Баширов',
#              'C++': 'Сидоров'}

# print('Язык программирования C++ изучает', languages['C' + '++'])

# info = dict(pupils = 'Сидоров', phone = 7123456789, town = 'Астрахань', gender = True)
# print(info)
# print(info['phone'])
# print(type(info))

# Создавать словари можно на основе списков кортежей или кортежей списков. Первый элемент списка или кортежа станет ключом, второй — значением.

# info_list = [('pupils', 'Сидоров'), ('phone', 7123456789), ('town', 'Астрахань')] # список кортежей
# print(info_list)

# info_dict = dict(info_list) # создаем словарь на основе списка кортежей
# print(info_dict)
# print(type(info_dict))
# info_tuple = (['pupils', 'Сидоров'], ['phone', 7123456789], ['town', 'Астрахань']) # кортеж списков

# info_dict = dict(info_tuple)  # создаем словарь на основе кортежа списков
# print(info_dict)
# Можно создать словарь, каждому ключу которого соответствует одно и то же значение, можно воспользоваться методом fromkeys().

# dict1 = dict.fromkeys(['name', 'age', 'job'])
# print(dict1)
# dict1 ['name'] = 'Ivan'
# print(dict1)
# dict1 ['name'] = 'Stas'
# print(dict1)
# dict1['gender'] = 'male'
# print(dict1)
# создает словарь с тремя элементами, где ключи — строки 'name', 'age', 'job', а соответствующие им значения: 'Missed information', 'Missed information', 'Missed information'.
# Пустой словарь
# Пустой словарь можно создать двумя способами:
# с помощью пустых фигурных скобок;
# с помощью функции dict().
# Приведенный ниже код:
# dict1 = {}
# dict2 = dict()

# print(dict1)
# print(dict2)
# print(type(dict1))
# print(type(dict2))

# Вывод словаря
# Для вывода всего словаря можно использовать функцию print():
# languages = {'Python': 'Иванов',
#              'C#': 'Петров',
#              'Java': 'Баширов',
#              'C++': 'Сидоров'}

# print(languages)


# info = {'name': 'Иван',
#         'age': 36,
#         'job': 'Механик',
#         'city': 'Воронеж',
#         'email': 'ivan@yandex.ru',
# 			'languages': {'Python': 'Иванов',
#              'C#': 'Петров',
#              'Java': 'Баширов',
#              'C++': 'Сидоров'}
# 			}

# # print(info['languages']['Python'])
# print(info['email'])


'''
Дан список студентов изучающих иностранный язык. Напишите код, который возвращает
список студентов, которые изучают Java."
'''
# from pprint import pprint
# languages = [
#             {'Иванов': ['Python','C#']},
# 			{'Иванов': ['C++', 'Java', 'C#']},
#             {'Петров': ['Python', 'Java']},
#             {'Баширов': ['C++','Python','Java', 'C#']},
#             {'Васин': ['C++','C#']},
#             {'Смирнов': ['Java','C#']}
#              ]
# lng_log = []
# for i in languages:
#   # print(i)
#   # print()
#     # j = i.values()
#   for j in i.values():
#     # print(j)
#     # print()
#     for s in range(len(j)):
#       if j[s] == 'Java':
#         lng_log.append(i)
# pprint(lng_log)


# Создание множества

# numbers = {2, 4, 6, 8, 10}
# languages = {'Python', 'C#', 'C++', 'Java'}
# print(type(numbers))


# info = {'IVAN', 1992, 1561.5}
# print(info)
# print(type(info))
# myset = set()   # пустое множество
# print(type(myset))
# myset = {}  # создается словарь

# # Вывод множества

# numbers = {2, 4, 6, 8, 10}
# languages = {'Python', 'C#', 'C++', 'Java'}
# mammals = {'cat', 'dog', 'fox', 'elephant'}

# print(*numbers)
# print(languages)
# print(mammals)

# {2, 4, 6, 8, 10}
# {'C#', 'Python', 'Java', 'C++'}
# {'dog', 'cat', 'fox', 'elephant'}

# # Встроенная функция set()

# myset1 = set(range(10+1))          # множество из элементов последовательности
# myset2 = set([1, 2, 3, 4, 4, 5])    # множество из элементов списка
# myset3 = set('abcd')             # множество из элементов строки
# myset4 = set((10, 20, 30, 40))   # множество из элементов кортежа
# print(myset1)
# print(myset2)
# print(myset3)
# print(myset4)
# emptyset1 = set([])  # пустое множество из пустого списка
# emptyset2 = set('')  # пустое множество из пустой строки
# emptyset3 = set(())  # пустое множество из пустого кортежа

# myset1 = {2, 2, 4, 6, 6}
# myset2 = set([1, 2, 2, 3, 3])
# myset3 = set('aaaaabbbbccccddd')

# print(myset1)
# print(myset2)
# print(myset3)

# myset = set(['aaa', 'bbbb', 'cc'])

# print(myset)

# myset = set('aaa bbbb cc')

# print(myset)

# myset1 = {1, 2, [5, 6], 7}    # множество не может содержать список
# myset2 = {1, 2, {5, 6}, 7}    # множество не может содержать множество

# TypeError: unhashable type: 'list'
# TypeError: unhashable type: 'set'


# myset = {1, 2, 5, (5, 6), 7}    # множество может содержать кортеж
# print(myset)

# languages = {
#             'Иванов': ['Python','C#'],
#             'Петров': ['Python', 'Java'],
#             'Васин': ['C++','Java'],
#             'Смирнов': ['Java','C#']
# }
# lset = set()
# for i in languages.values():
#   for j in i:
#     lset.add(j)
# print(*lset)

# st = 'hello , my name is Peter, I am 26 years old'
# print(len(st))
# print(st.split())
# print(len(st.split()))
# a = st.split()
# print(len(a))

# true_war = True
# false_war = False

# print(not true_war == false_war)
# print(true_war == (not false_war))
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
]
mylist = []
for k in queries:
    mylist.append(len(k.split()))
print(mylist)
# '1':11 проц
# '2':33 проц
# '3':44 проц
# '4':11 проц
# stats = {'yandex': 120, 'vk': 155, 'google': 99, 'email': 42, 'ok': 98, 'no': 150}
# mylist = []
# max_ = 0
# name = ''
# for v, k in stats.items():
#     mylist.append(s)
# print(mylist)

