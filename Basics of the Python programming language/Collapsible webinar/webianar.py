from math import inf
from pprint import pprint

# списковое включение
# start = 0
# finish = 10
# cnt = 0
# num_list = []

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# while cnt <= finish:
#     num_list.append(cnt ** 2)
#     print(num_list)
#     cnt += 1

# print(list(range(11)))

# for cnt in range(11):
#     num_list.append(cnt ** 2)
#     print(num_list)

# списковое включение
# print([str(cnt ** 2) + "ABC" for cnt in range(11) if cnt % 2 == 0 and cnt ** 2 != 36])
# print({str(cnt ** 2) + "ABC" for cnt in range(11) if cnt % 2 == 0 and cnt ** 2 != 36})
# print({key + 100: value - 100 for key, value in ([1, 2], [3, 4], [5, 6])})
# print((str(cnt ** 2) + "ABC" for cnt in range(11) if cnt % 2 == 0 and cnt ** 2 != 36))


# class EmailNotifier:
#     def notify(self, msg):
#         print(f"Канал оповещения через почту. Оповещаю администратора площадки сообщением: {msg}")
#
#
# class TelegramNotifier:
#     def notify(self, msg):
#         print(f"Канал оповещения через телеграм. Оповещаю администратора площадки сообщением: {msg}")
#
#
# class SmsNotifier:
#     def notify(self, msg):
#         print(f"Канал оповещения через SMS. Оповещаю администратора площадки сообщением: {msg}")
#
#
# class ConsoleNotifier:
#     def notify(self, msg):
#         print(f"Канал оповещения через консоль. Оповещаю администратора площадки сообщением: {msg}")
#
#
# class TickertSeller:
#     def __init__(self, seller_name, notifiers_list=None):
#         if notifiers_list is None:
#             notifiers_list = [ConsoleNotifier(), ]
#         self.seller_name = seller_name
#         self.notifiers_list = notifiers_list
#
#     def sell_ticket(self, name):
#         print("Какая-то логика по продаже билетов на стороне селлера", self.seller_name)
#         msg = f"{self.seller_name} продал билет покупателю: {name}"
#         for notifier in self.notifiers_list:
#             notifier.notify(msg=msg)
#
#
# email_notifier = EmailNotifier()
# telegram_notifier = TelegramNotifier()
# sms_notifier = SmsNotifier()
# console_notifier = ConsoleNotifier()
# notifiers_list = [email_notifier, telegram_notifier, sms_notifier]
# ticket_seller = TickertSeller(notifiers_list=notifiers_list, seller_name="Tommy Vercetti")
# ticket_seller.sell_ticket("Nikolai Sviridov")
#
# print("################################################")
#
# ticket_seller_2 = TickertSeller(seller_name="Geralt of Rivia")
# ticket_seller_2.sell_ticket("Mike Tyson")


# user_list = [
#     {"user_id": 1,
#      "age": 18,
#      "privileges": []
#      },
#     {"user_id": 2,
#      "age": 1,
#      "privileges": []
#      },
#     {"user_id": 3,
#      "age": 6,
#      "privileges": []
#      },
#     {"user_id": 4,
#      "age": 22,
#      "privileges": []
#      }
# ]
#
# discount_for_flight_tickets = "discount_for_flight_tickets"
# buy_alco = "buy_alco"
#
#
# def grant_privileges_to_users(user_list, privilege, start_age, end_age):
#     for user in user_list:
#         if start_age <= user["age"] <= end_age:
#             user["privileges"].append(privilege)
#
#
# def revoke_privileges_from_users(user_list, privilege):
#     for user in user_list:
#         if privilege in user["privileges"]:
#             user["privileges"].remove(privilege)
#
#
# grant_privileges_to_users(user_list=user_list, privilege=discount_for_flight_tickets, start_age=0, end_age=12)
# grant_privileges_to_users(user_list=user_list, privilege=buy_alco, start_age=18, end_age=inf)
# pprint(user_list)
#
# revoke_privileges_from_users(user_list=user_list, privilege=buy_alco)
# pprint(user_list)
#
# grant_privileges_to_users(user_list=user_list, privilege=buy_alco, start_age=21, end_age=inf)
# pprint(user_list)

class Box:
    def __init__(self):
        self.compound = []

    def add_into(self, some_object):
        self.compound.append(some_object)

    def give_me_number_of_stuff(self):
        return len(self.compound)

    def __str__(self):
        return f"Состав ящика: {self.compound}"

    def __repr__(self):
        return f"Состав ящика: {self.compound}"

    def __lt__(self, other):
        return self.give_me_number_of_stuff() < other.give_me_number_of_stuff()


class Tumbochka:
    def __init__(self):
        self.boxes = {
        }

    def put_into(self, some_object, box_key):
        if box_key not in self.boxes:
            print("Такого ящика не существует, выберите другой!")
        else:
            self.boxes[box_key].add_into(some_object)

    def add_new_box(self, box_key, box):
        if box_key in self.boxes:
            print("Такой ящик уже есть, выберите другой ключ!")
        else:
            self.boxes[box_key] = box

    def __str__(self):
        return f"Состав тумбочки: {self.boxes}"
#
#
# tumbochka_1 = Tumbochka()
# print(tumbochka_1)
# box_1 = Box()
# print(box_1)
# tumbochka_1.add_new_box(box_key="some_box", box=box_1)
# print(tumbochka_1)
# some_object = 123
# tumbochka_1.put_into(some_object=some_object, box_key="some_box")
# print(tumbochka_1)
# box_2 = Box()
# tumbochka_1.add_new_box(box_key="some_box_2", box=box_2)
# print(tumbochka_1)
# tumbochka_2 = Tumbochka()
# print(tumbochka_2)
#
# print(box_1 < box_2)


# def get_last_element(some_list):
#     return some_list[-1]

get_last_element = lambda some_list: some_list[-1]


my_list = [1, 2, 3, 4, 5]
my_list_of_lists = [
    [1, 2],
    [2, -10],
    [100, 1000],
    [-100, 90]
]
my_list_of_lists.sort(key=lambda some_list: some_list[-1])
print(my_list_of_lists)
# print(get_last_element(my_list))


class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b