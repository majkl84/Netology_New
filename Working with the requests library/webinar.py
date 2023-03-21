from pprint import pprint

import requests

# res = requests.get("http://google.com")
# print(res)
# print(res.text)


# params = {"region_guid": "1d1463ae-c80f-4d19-9331-a1b68a85b553"}
# res = requests.get("https://search-suggest.domclick.ru/api/subways/v1", params=params)
# pprint(res.json())


# body = {"locationId": 621540, "query": "вакансии"}
# res = requests.post("https://www.avito.ru/web/3/suggest", json=body, headers=headers)
# print(res)


TOKEN = "y0_AgAAAAAILgNiAAmJmAAAAADfDj36iX0w67QIS1mm9hzERtKvzkwYKuU"
headers = {
            "Content-Type": "application/json",
            "Authorization": "OAuth y0_AgAAAAAILgNiAAmJmAAAAADfDj36iX0w67QIS1mm9hzERtKvzkwYKuU"
          }

# res = requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=%D0%BD%D0%B5%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F2", headers=headers)
res = requests.get("https://cloud-api.yandex.net/v1/disk/", headers=headers)
print(res.text)

"""
https://oauth.yandex.ru/client/new - создать приложение
https://yandex.ru/dev/direct/doc/start/token.html - как получить oauth-token
https://yandex.ru/dev/disk/poligon/ - Яндекс Полигон
https://oauth.yandex.ru/verification_code - эту ссылку нужно вставить при создании приложения в поле Redirect URI
https://oauth.yandex.ru/authorize?response_type=token&client_id=ИДЕНТИФИКАТОР_ПРИЛОЖЕНИЯ - ссылка для получения токена
https://yandex.ru/dev/disk/api/reference/upload.html - как загружать файл на Диск через запросы
"""


import requests

headers = {
            "Content-Type": "application/json",
            "Authorization": "OAuth "
          }

# resp = requests.get("https://cloud-api.yandex.net/v1/disk", headers=headers)
# print(resp.json())

params = {
    "path": "моя_папка"
}

resp = requests.put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
print(resp)