import requests
# y0_AgAAAAAILgNiAADLWwAAAADfEGpsadQAxv4fQZmz9k1TBGpT5eyEhco
hero_list = ('Hulk', 'Captain America', 'Thanos')
# def hero(heroes: list):
#     heroes_dict = {}
#     url = 'https://akabab.github.io/superhero-api/api'
#     resp = requests.get(f'{url}/all.json')
#     if resp.status_code != 200:
#         return "Неверный код или ошибка на сервере."
#     hero = resp.json()
#     for best_hero in hero:
#         print(best_hero)
#         name_hero = heroes_dict[hero]
#         if name in heroes_dict():
#             heroes_dict += name
#     name_hero, smart_hero = max(heroes_dict.items(), key=lambda x: heroes_dict[1])
#     result = (f'\nСамый умный супергерой: {best_hero} - его интелект: {smart_hero} ')
#     return result
#
# print(hero(hero_list))


HERO_IDS = {
    'Hulk': 332,
    'Captain America': 149,
    'Thanos': 655,
}

hero_intelligence = {}
for hero_name, hero_id in HERO_IDS.items():
    response = requests.get(f'https://akabab.github.io/superhero-api/api/powerstats/{hero_id}.json')
    data = response.json()
    intelligence = data['intelligence']
    hero_intelligence[hero_name] = int(intelligence)
print(hero_intelligence)
smartest_hero = max(hero_intelligence, key=hero_intelligence.get)

print(f'Самый умный супергерой - это {smartest_hero} с интеллектом {hero_intelligence[smartest_hero]}.')

