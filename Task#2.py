def read_file_in_dict():
    cook_book = {}
    quantity_ingredients = 0
    flag = True
    with open("recipes.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.rstrip('\n'):
                if quantity_ingredients == 0 and flag:
                    dish = line.rstrip('\n')
                    cook_book[dish] = []
                    flag = False
                elif quantity_ingredients == 0 and not flag:
                    quantity_ingredients = int(line.rstrip('\n'))
                else:
                    ingridient = line.rstrip('\n').split(" | ")
                    cook_book[dish].append({'ingredient_name': ingridient[0],
                                            'quantity': int(ingridient[1]),
                                            'measure': ingridient[2]})
                    quantity_ingredients -= 1
                    if quantity_ingredients == 0:
                        flag = True
        return cook_book

def counting_ingredients_for_person(ingredient_dish, person_count):
    result = {}
    result['measure'] = ingredient_dish['measure']
    result['quantity'] = ingredient_dish['quantity'] * person_count
    return result

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_file_in_dict()
    ingredients = {}
    for dish in dishes:
        for ingredient_dish in cook_book[dish]:
            ingredients[ingredient_dish['ingredient_name']] = counting_ingredients_for_person(ingredient_dish, person_count)
    print(ingredients)


get_shop_list_by_dishes(['Омлет'], 2)