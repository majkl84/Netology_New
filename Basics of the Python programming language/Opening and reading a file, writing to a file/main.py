from pprint import pprint
cook_book = {}
def get_cook_book():

    with open("recipes.txt",encoding="utf-8") as file_with_food:
        while True:
            name = file_with_food.readline().strip()
            if not name:
                break
            count = int(file_with_food.readline().strip())
            cook_book[name] = []
            line = file_with_food.readline().strip()
            while line:
                ingredients = line.split(" | ")
                ingredients_dict = {"ingredient_name": ingredients[0],
                                    "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[name].append(ingredients_dict)
                line = file_with_food.readline().strip()
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def sorted_files(files):
    count_list = []
    for item_file in files:
        with open(item_file, encoding='utf-8') as fl:
            text = fl.readlines()
            len_text = len(text)
            name = fl.name
            count_list.append([text, name, len_text])
    count_list.sort(reverse=True)

    with open("text.txt", "w", encoding='utf-8') as ff:
        for item in count_list[:]:
            new_path = item[1].replace("source/", "")
            ff.write(new_path + "\n")
            ff.write(str(item[2]) + "\n")
            for j in item[0]:
                ff.write(j.strip() + "\n")
    print("файл сохранен /text.txt")

print(get_cook_book())
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print(sorted_files(['1.txt', '2.txt', '3.txt']))






