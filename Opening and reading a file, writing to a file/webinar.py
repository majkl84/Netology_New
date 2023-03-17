# print(open)
# from io import TextIOWrapper

# file_object = open("sample_file.txt", "r")
# print(file_object)
# data_from_file_by_read_method = file_object.read()
# print(type(data_from_file_by_read_method), "\n", data_from_file_by_read_method)
# data_from_file_by_read_method_1 = file_object.read()
# print("сейчас курсор:", file_object.tell())
# print("повторное чтение...")
# file_object.seek(0)
# print("сейчас курсор:", file_object.tell())
# print(data_from_file_by_read_method_1)
# print("чтение завершено")

# next_line = None
# while True:
#     next_line = file_object.readline()
#     if next_line == "":
#         break
#     print(next_line)
#     print("сейчас курсор:", file_object.tell())

# lines_from_file = file_object.readlines()
# print(lines_from_file)

# for line in file_object:
#     print(line, end="")

# file_object = open("test_file.txt", "w")
# string_for_write = """user_1
# Nikolai | Sviridov | Developer
#
# user_2
# Petr | Petrov | QA manual"""
# file_object.write(string_for_write)
# str_1 = "abc"
# str_2 = "def"
# file_object.write(str_1 + "\n")
# file_object.write(str_2)

# data_for_write = ['user_1\n', 'Nikolai | Sviridov | Developer\n', '\n', 'user_2\n', 'Petr | Petrov | QA manual']
# file_object.writelines(data_for_write)

# file_object = open("sample_file.txt", "a")
# string_for_write = """
# user_3
# Nikolai | Sviridov | Developer
#
# user_4
# Petr | Petrov | QA manual
# """
# file_object.write(string_for_write)

"""
user_data_list = [
            {
                "user_id": "user_1",
                "name": "Nikolai",
                "surname": "Sviridov",
                "position": "Developer"
            },
            {
                "user_id": "user_2",
                "name": "Petr",
                "surname": "Petrov",
                "position": "QA Manual"
            }
]
"""
from pprint import pprint

"""user_data_list = [
    {
        "user_1":
            {
                "name": "Nikolai",
                "surname": "Sviridov",
                "position": "Developer"
            },
    },
    {
        "user_2":
            {
                "name": "Petr",
                "surname": "Petrov",
                "position": "QA Manual"
            }
    }
]"""

"""users_data_dict = {
        "user_1":
            {
                "name": "Nikolai",
                "surname": "Sviridov",
                "position": "Developer"
            },
        "user_2":
            {
                "name": "Petr",
                "surname": "Petrov",
                "position": "QA Manual"
            }
}"""

# users_data_dict = {}
# with open("sample_file.txt", "r") as file_with_users:
#     data_from_file = file_with_users.read()
#     splitted_user_info = data_from_file.split("\n\n")
#     print(splitted_user_info)
#     for user_data in splitted_user_info:
#         user_id, user_personal_data = user_data.split("\n")
#         name, surname, position = user_personal_data.split("|")
#         user_dict = {
#             "name": name,
#             "surname": surname,
#             "position": position
#         }
#         users_data_dict[user_id] = user_dict

# pprint(users_data_dict)
# print(users_data_dict["user_1"])

try:
    1 / 0
except ZeroDivisionError:
    print("вы поделили на ноль. так не надо делать, но я продолжу работу все равно")
print("Пограмма завершена")