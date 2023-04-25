# raise ZeroDivisionError

# def insert_user(_id, name):
#     print("Пытаемся записать пользователя в нашу БД")
#     raise Exception("Такой пользователь уже существует")
#
#
# """
# |id | name |
#  1     Petr
#  2     Nick
#  1     Maria
# """

# try:
#     insert_user(1, "Sample Name")
# except Exception:
#     print("Такой юзер уже есть")
#
# print("Программа пошла работать дальше")

# while True:
#     file_name = input("Введите имя файла: ")
#     try:
#         with open(file_name):
#             print("Работаем с файлом")
#     except FileNotFoundError:
#         print("Видимо вы указали несуществующее имя файла:", file_name)
#     answer = input("Хотите повторить ввод? ")
#     if answer.lower() not in {"да", "yes", "y", "1"}:
#         break


# Формат CSV - плоские данные
import csv
from pprint import pprint


# def read_csv(file_name: str):
#     with open(file_name) as csv_file:
#         reader = csv.reader(csv_file)
#         print(reader)
#         data = list(reader)
#         print(data)
#     header = data.pop(0)
#     print(header)
#     return header, data

# read_csv("sample.csv")


# def write_csv(in_file_name: str, out_file_name: str):
#     header, data = read_csv(in_file_name)
#
#     with open(out_file_name, "w") as file:
#         writer = csv.writer(file, delimiter="*")
#         writer.writerow(header)
#         writer.writerows(data)


# write_csv("sample.csv", "sample_new.csv")
# read_csv_as_dict("sample.csv")

def read_csv_as_dict(file_name: str):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)
        # pprint(list(reader))
        for item in reader:
            print(item)


read_csv_as_dict("sample.csv")

# Формат json - древовидная структура
import json


def read_json(file_name: str):
    with open(file_name) as file_object:
        data = json.load(file_object)
        return data


def write_json(in_file_name: str, out_file_name: str):
    data = read_json(in_file_name)
    with open(out_file_name, "w") as file_object:
        json.dump(data, file_object, ensure_ascii=False, indent=2)


# pprint(read_json("data.json"))
# write_json("data.json", "data_new.json")


# Формат XML - древовидная структура
import xml.etree.ElementTree as ET  # модуль для работы с XML
from xml.dom import minidom  # штука для взаимодействия с XML

# parser = ET.XMLParser(encoding="utf-8")  # получаем объект-парсер
# tree = ET.parse("sample.xml", parser)  # получаем некое дерево элементов из парсера
# root = tree.getroot()  # получаем из дерева его корень
# print(root.text, root.tag, root.attrib["version"])

# books_list = root.findall("book")  # найти все книги
# author_list = root.findall("book/author")  # найти всех авторов внутри книг
# print(len(books_list), len(author_list))
# pprint(author_list)
# print(books_list)
# print(author_list)

# for book in books_list:  # найти в каждой книге автора и вывести id
#     # print(book.find("author"))
#     author = book.find("author")
#     if author is not None:
#         print(author.text)
#     print(book.attrib["id"])


# byte_xml_string = ET.tostring(root)
# как записать новую XML-ку?
# print(byte_xml_string)
# xmlstr = minidom.parseString(byte_xml_string).toprettyxml()
# print(xmlstr)
# with open("result.xml", "w") as file_object:
#     file_object.write(xmlstr)