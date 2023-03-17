# print(2**200000)
# print(16 % 3)

# region = input("Введите область: ")
# if region == 'Сахалинский край' or region == 'Камчатский округ' or region == 'Республика Саха':
#        district = 'Дальний восток'
#        print(district)
# number = 10
# print(type(number))
# q = 9.8
# print(type(q))
# name = 'Коля'
# print(type(name))
# sun = True
# print(type(sun))
# q = bool(q)
# print(q)
# print(type(q))

# преобразование типов

# q = 9.8
# print(type(q))
# print(q)
# print('---------------------')
# q = int(q)
# print(type(q))
# print(q)
# print('---------------------')
# q = float(q)
# print(type(q))
# print(q)
# print('---------------------')
# q = bool(q)
# print(type(q))
# print(q)
# print('---------------------')
# q = str(q)
# print(type(q))
# print(q)


# неявное преобразование
# c = 8 // 4
# b = 5 + True + True + True + True

# print(c)
# print(b)
# print(type(b))
# b = 15.6
# print(type(b))

# b = 'eeee'
# print(type(b))

# Строки

# greeting = 'Hello, my names is Oleg!'
# print(greeting)
# print(len(greeting))
# print(greeting[5])
# print(greeting[-5])

# greeting[-4] = 'H'
# объект не поддерживает назначение элемента

# greeting1 = greeting[:18]
# print(greeting[:18])
# print(greeting)
# print(greeting1)
# greeting1 += ' Nicolas!'
# print(greeting1 + ' Nicolas!')
# print(greeting1)

# greeting2 = greeting[::3] # Шаг
# print(greeting2)
# print(greeting[::-1])

# Списки

# int_list = [1, 2, 3, [1, 2.0, 'string']]

# mixed_list = [1, 2.0, 'string']

# print(len(int_list))

# print(int_list[3])
# print(int_list[3][2][-2])

# print(int_list[::-1])

# names1 = ['John', 'Bob', 'Alice']
# names2 = ['Tracy', 'Elijah', 'Mason']

# print(names1 + names2)
# names2 = names2 + names1
# print(names2)
# names1[0] = [1, 2.0, 'string']
# print(names1)

# names1.append('William')
# names1.append('James')
# print(names1)
# lst = []
# lst1 = input().split()
# print(lst1)
# print(type(lst1))
# popped = names1.pop() #same as names1.pop(-1)
# print(popped)
# print(names1)

# names1.append('James')
# names1.sort()
# print(names1)
# names1.append('5James')
# print(names1)
# names1.sort()
# print(names1)
# names_people = [['John', 'Bob', 'Alice'], ['Tracy', 'Elijah', 'Mayson']]
# print(names_people[0][2])

# Кортежи
# a = tuple() # С помощью встроенной функции tuple()
# a = () # С помощью литерала кортежа

# person = ('John', 'Silver', 22)
# print(type(person))

# person_info = ['John', 'Silver', 22]
# print(type(person_info))
# print(len(person))

# print(person[0])
# print(person[-1])

# person_info[0]="Bob"
# print(person_info)

# person[0] = "Bob"

# цикл while
# x = 0
# a = 1
# a = a + 1
# print(a)
# a = a + 1
# print(a)

# while True:
# 	x += 3
#	print(f'x equals: {x}')
# 	print('x equals:', x)


# x = 0

# while x <= 21:
#     print(f'x equals {x}')
#     x+=3
# else:
#     print('Условие не выполнено, цикл закончен', x)


# Break, Continue, Pass

# vals = [1,2,3,4,5,6,7,8,9]

# sum_ = 0 # рассказать про использование зарезервированных слов
# for v in vals:
#     if v % 2 == 0:
#         continue
#     else:
#         sum_ += v
#     if sum_ >= 10:
#         break

# print(sum_)

# for v in vals:
#     pass

# numbers = [2,2,8,4,5]
# for i in (numbers):
#     print('Индекс', i, 'Значение', numbers[i])

# numbers = range(6)

# for i in numbers:
#     print(i)

# for i in range(1, 6):
#     print(i)

# for i in range(1, 6):
#     if i % 2 == 0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')

# numbers = [1,3,5,7,9]
# for i in range(len(numbers)):
#     numbers[i] **= 2
#     print(i, numbers[i])


# name = "John"
# for st_char in name:
#     print(st_char)

# for _ in range(5):
#     print('Alarm!', _)


# # For and Tuples

# person = ('John', 'Silver', 22)
# for item in person:
#     print(item)

# #many funcs return list of tuples
# persons = [('John', 22), ('Bob', 32), ('Dave', 20)]
# print(len(persons))

# # #tuple unpacking
# # #for name, age in persons:
# for (name, age) in persons:
# 	print(f'{name} is {age} years old')
# 	print(name, 'is', age, 'years old')

# find all pairs sum of which equals 0
list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]
# list1.sort()
# list2.sort()

# pairs = []
# for x in list1:
#     for y in list2:
#         cur_sum = x + y
#         if cur_sum == 0:
#             pairs.append((x, y))
# print(pairs)
# for name, number in zip(list1, list2):
#   print(name, number, sep = ':', end = '|')
new_tuple = zip(list1, list2)
print(new_tuple)
a = list(new_tuple)
b = tuple(new_tuple)
print(a)
print(b)
# employee_numbers = [2, 9, 18, 28, 56]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]

# for name, number in zip(employee_names, employee_numbers):
# 	print(name, number)