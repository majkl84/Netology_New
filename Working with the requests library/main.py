import requests

hero_list = ['Hulk', 'Captain America', 'Thanos']
# def gero_intelligence(hero_person):
#     hero_intelligence = {}
#     url = 'https://akabab.github.io/superhero-api/api'
#     resp = requests.get(f'{url}/all.json')
#     if resp.status_code != 200:
#         return "Неверный код или ошибка на сервере."
#     for i in resp.json():
#         if i['name'] in hero_person:
#             hero_intelligence[i['name']] = i['powerstats']['intelligence']
#     smartest_hero = max(hero_intelligence, key=hero_intelligence.get)
#     return f'Самый умный супергерой - это {smartest_hero} с интеллектом {hero_intelligence[smartest_hero]}.'
#
# print(gero_intelligence(hero_list))
class YaUploader:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"OAuth {self.token}"}
    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path}
        with open(file_path, "rb") as file_path:
            response = requests.get(url=url, headers=self.headers, params=params)
            if response.status_code != 200:
                return False
            upload_url = response.json().get("href")
            response = requests.put(upload_url, headers=self.headers, data=file_path)
            return response.status_code == 201

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = 'y0_AgAAAAAILgNiAADLWwAAAADfEGpsadQAxv4fQZmz9k1TBGpT5eyEhco'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
