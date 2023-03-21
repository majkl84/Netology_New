import requests
# y0_AgAAAAAILgNiAADLWwAAAADfEGpsadQAxv4fQZmz9k1TBGpT5eyEhco

hero_list = ['Hulk', 'Captain America', 'Thanos']
def gero_intelligence(hero_person):
    hero_intelligence = {}
    url = 'https://akabab.github.io/superhero-api/api'
    resp = requests.get(f'{url}/all.json')
    if resp.status_code != 200:
        return "Неверный код или ошибка на сервере."
    for i in resp.json():
        if i['name'] in hero_person:
            hero_intelligence[i['name']] = i['powerstats']['intelligence']
    smartest_hero = max(hero_intelligence, key=hero_intelligence.get)
    return f'Самый умный супергерой - это {smartest_hero} с интеллектом {hero_intelligence[smartest_hero]}.'

print(gero_intelligence(hero_list))