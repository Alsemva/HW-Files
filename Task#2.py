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


print(read_file_in_dict())
