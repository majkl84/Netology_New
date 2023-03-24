"""
https://oauth.vk.com/authorize?client_id=51420426&display=page&scope=stats.offline&response_type=token&v=5.131
"""

with open("token.txt", "r") as file_object:
    token = file_object.read().strip()

# print(token)

import requests
from pprint import pprint


# URL = "https://api.vk.com/method/users.get"
# params = {
#     "user_ids": "1, 2",
#     "access_token": token,
#     "v": "5.131",
#     "fields": "education, sex"
# }
# res = requests.get(URL, params=params)
# pprint(res.json())


# получаем список групп по поисковому запросу
# def search_group(query: str, sorting=0):
#     """
#     0 - сортировка по умолчанию
#     1 - сортировка по скорости роста
#     2 - отношение дневной посещаемости
#     3 - отношение количества лайков к количеству пользователей
#     4 - комментариев к количеству пользователей
#     5 - записей в обсуждениях к количеству пользователей
#     """
#     params = {
#         "q": query,
#         "access_token": token,
#         "v": "5.131",
#         "sort": sorting,
#         "count": 300
#     }
#     resp = requests.get("https://api.vk.com/method/groups.search", params).json()
#     response_data = resp["response"]["items"]
#     return response_data
#
#
# target_groups = search_group("python")
# pprint(target_groups)

# # расширенная информация о группе
# target_group_ids = "1, 2, 3, 4, 5"
# params = {
#     "access_token": token,
#     "v": "5.131",
#     "group_ids": target_group_ids,
#     "fields": "members_count, activity, description"
# }
# resp = requests.get("https://api.vk.com/method/groups.getById", params)
# pprint(resp.json()["response"])


# теперь напишем класс для взаимодействия с VkAPI
class VkApiClient:
    CNT = 0

    def __init__(self, token: str, api_version: str, base_url: str = "https://api.vk.com/"):
        self.token = token
        self.api_version = api_version
        self.base_url = base_url

    def general_params(self):
        return {
            "access_token": self.token,
            "v": self.api_version,
        }

    def get_users_info(self, user_ids: str, fields: str):
        params = {
            "user_ids": user_ids,
            "fields": fields,
        }
        params.update(self.general_params())
        return requests.get(f"{self.base_url}/method/users.get",
                            params=params).json()

    def search_group(self, query: str, sorting: int = 0, count: int = 5):
        """
        0 - сортировка по умолчанию
        1 - сортировка по скорости роста
        2 - отношение дневной посещаемости
        3 - отношение количества лайков к количеству пользователей
        4 - комментариев к количеству пользователей
        5 - записей в обсуждениях к количеству пользователей
        """
        params = {
            "q": query,
            "sort": sorting,
            "count": count
        }
        params.update(self.general_params())
        return requests.get(f"{self.base_url}/method/groups.search",
                            params=params).json()["response"]["items"]

    def additional_group_info(self, target_group_ids: str, fields: str):
        self.CNT += 1
        params = {
            "group_ids": target_group_ids,
            "fields": fields
        }
        params.update(self.general_params())
        return requests.get(f"{self.base_url}/method/groups.getById",
                            params=params).json()["response"]


vk_client = VkApiClient(token=token, api_version="5.131")
for _ in range(5):
    pprint(vk_client.additional_group_info(target_group_ids="1, 2, 3, 4, 5, 6",
                                           fields="members_count, activity, description"))
print(f"Метод additional_group_info был использован {vk_client.CNT} раз за работу программы.")