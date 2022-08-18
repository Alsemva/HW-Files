def read_file_in_dict():
    cook_book = {}
    quantity_ingredients = 0
    flag = 0
    with open("recipes.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.rstrip():
                if quantity_ingredients == 0 and flag == 0:
                    dish = line.rstrip()
                    cook_book[dish] = []
                    flag = 1
                elif quantity_ingredients == 0 and flag == 1:
                    quantity_ingredients = int(line.rstrip())
                else:
                    ingridient = line.rstrip().split(" | ")
                    cook_book[dish].append({'ingredient_name': ingridient[0],
                                            'quantity': int(ingridient[1]),
                                            'measure': ingridient[2]})
                    quantity_ingredients -= 1
                    if quantity_ingredients == 0:
                        flag = 0
        return cook_book


print(read_file_in_dict())
