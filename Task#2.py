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


def counting_ingredients_for_person(ingredient_dish, person_count, temp):
    result = {}
    result['measure'] = ingredient_dish['measure']
    result['quantity'] = ingredient_dish['quantity'] * person_count + temp
    return result


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_file_in_dict()
    ingredients = {}
    temp = 0
    for dish in dishes:
        for ingredient_dish in cook_book[dish]:
            if ingredient_dish['ingredient_name'] in ingredients:
                temp = ingredients[ingredient_dish['ingredient_name']]['quantity']
            ingredients[ingredient_dish['ingredient_name']] = \
                counting_ingredients_for_person(ingredient_dish, person_count, temp)
            temp = 0
    return ingredients


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
