from pprint import pprint
cook_book = {}
with open("../recipes.txt", encoding="utf-8") as file_with_food:
    recipes_from_the_file = file_with_food.read()
    recipe_information = recipes_from_the_file.split("\n")
    print(recipe_information)
    for cook_book_data in recipe_information:
        name_recipe, person, ingredients = cook_book_data.split(" ")
        print(name_recipe)
        ingredient_name, quantity, measure = ingredients.split("|")
        ingredients = {
            "ingredient_name": ingredient_name,
            "quantity": quantity,
            "measure": measure
        }
        cook_book[name_recipe] = ingredients

pprint(cook_book)
print(cook_book["Омлет"])