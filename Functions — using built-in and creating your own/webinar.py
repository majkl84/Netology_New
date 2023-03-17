
# def square(number):
#   result = number ** 2
#   # print(result)
#   return result

# res = square(40)
# res = res / 5
# print(res)

# help(print)

# def function(a, b):
#   """
#   function(a, b) -> list
#   функция преобразует два числа в список
#   """
#   return [a, b]
# help(function)
# print(function(20, 15))

# def square():
#   number = int(input('Введите число'))
#   square_num = number ** 2
#   return square_num

# print(square())

# def power(number=15, number_2=2):
#   square_num = number ** number_2
#   result_2 = number * number_2
#   result_3 = number / number_2
#   return square_num, result_2, result_3

# print(*power(10))
# print(*power(15))
# print(*power(5.5, 1.02))


# name = 'James'

# def say_hi(name):
# 	# name = 'Oleg'
# 	# global name
# 	# name = 'Oleg'
# 	some_str = '11111'
# 	print('Hello', name)

# say_hi(name)
# print('Hello', name)

# print(some_str = '11111')


# name = 'Игорь'
# def say_hi():
#   name = 'Oleg'
#   def get_name():
#     nonlocal name
#     name = input('Введите имя')
#     return name
#   get_name()
#   print('Hello', name)


# say_hi()
# print(name)


# def defined_cube(y):
#     return y*y*y

# lambda_cube = lambda y: y*y*y
# print(defined_cube(2))
# print(lambda_cube(2))

# def func(x, y, z):
# 	r = x + y + z
# 	c = x * y * z
# 	return r,c

# print(func(2, 5, 7))

students_list = [
    {"name": "Василий", "surname": "Теркин", "gender": "м", "program_exp": True, "grade": [8, 8, 9, 10, 9], "exam": 8},
    {"name": "Мария", "surname": "Павлова", "gender": "ж", "program_exp": True, "grade": [7, 8, 9, 7, 9], "exam": 9},
    {"name": "Ирина", "surname": "Андреева", "gender": "ж", "program_exp": False, "grade": [10, 9, 8, 10, 10], "exam": 7},
    {"name": "Татьяна", "surname": "Сидорова", "gender": "ж", "program_exp": False, "grade": [7, 8, 8, 9, 8]
     ,"exam": 10},
    {"name": "Иван", "surname": "Васильев", "gender": "м", "program_exp": True, "grade": [9, 8, 9, 6, 9], "exam": 7},
    {"name": "Роман", "surname": "Золотарев", "gender": "м", "program_exp": False, "grade": [8, 9, 9, 6, 9], "exam": 6}
]

def get_avg_exam_grade(students):
    sum_ex = 0
    for student in students:
        # print(student)
        sum_ex += student['exam']
    return round(sum_ex / len(students), 2)

# print(f'Средняя оценка за экзамен {get_avg_exam_grade(students_list)}')

def get_avg_hw_grade(students):
    sum_hw = 0
    for student in students:
        sum_hw += sum(student['grade']) / len(student['grade'])
    return round(sum_hw / len(students), 2)

# print(get_avg_hw_grade(students_list))

def main(stud):
    while True:
        user_input = input('Введите команду')
        if user_input == '1':
            print(get_avg_exam_grade(stud))
        elif user_input == '2':
            print(get_avg_hw_grade(stud))
        elif user_input == 'q':
            print('До свидания!')
            break


main(students_list)