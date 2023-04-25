# def discriminant(a, b, c):
#     return b ** 2 - 4 * a * c

# def solution(a, b, c):

#     result = discriminant(a, b, c)
#     if result < 0:
#         print('корней нет')
#     elif result == 0:
#         decision = -b / (2 * a)
#         print(f'{decision}')
#     else:
#         decision_1 = (-b + result ** 0.5) / (2 * a)
#         decision_2 = (-b - result ** 0.5) / (2 * a)
#         if (decision_1 < decision_2):
#             print(f'{decision_1} {decision_2}')
#         else:
#             print(f'{decision_2} {decision_1}')
# # не меняйте эту часть программы
# # вывод решения для коэфициентов, заданных в условии задачи
# solution(-1, -2, 15)
# solution(1, -13, 12)
# solution(-4, 28, -49)
# solution(1, 1, 1)

##################Задание - 2################################################
# def vote(votes):
#     d = {}
#     for v in votes:
#         c = votes.count(v)
#         d.setdefault(v, c)

#     m = d.values()
#     i = max(m)
#     for name, value in d.items():
#        if value == i:
#            return name

# print(vote([1,1,1,2,3]))
# print(vote([1,2,3,2,2]))

##################Задание - 3################################################
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    for i in documents:
        if i['number'] == doc_number:
            return (i['name'])
    if i['number'] != doc_number:
        return 'Документ не найден'


def get_directory(doc_number):
    for key, value in directories.items():
        if doc_number in value:
            return key

    return 'Полки с таким документом не найдено'


def add(document_type, number, name, shelf_number):
    shelf = str(shelf_number)
    new_dict = dict(type=document_type, number=number, name=name)
    documents.append(new_dict)
    directories[shelf] += [number]


print(get_name("10006"))
print(get_directory("11-2"))
print(get_name("101"))
add('international passport', '311 020203', 'Александр Пушкин', 3)
print(get_directory("311 020203"))
print(get_name("311 020203"))
print(get_directory("311 020204"))
