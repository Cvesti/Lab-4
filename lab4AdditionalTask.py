#Предметы и их характеристики
ITEMS = {
    'r': (3, 25),  #Винтовка
    'p': (2, 15),  #Пистолет
    'a': (2, 15),  #Боекомплект
    'm': (2, 20),  #Аптечка
    'i': (1, 5),   #Ингалятор
    'k': (1, 15),  #Нож
    'x': (3, 20),  #Топор
    't': (1, 25),  #Оберег
    'f': (1, 15),  #Фляжка
    'd': (1, 10),  #Антидот
    's': (2, 20),  #Еда
    'c': (2, 20),  #Арбалет
}

MAX_CELLS = 7       
MIN_POINTS = 0      
INITIAL_POINTS = 10 
REQUIRED_ITEMS = ['i']  #Необходимый ингалятор

def choose_items(selected_items, item_keys, start_index):
    total_weight = sum(ITEMS[item][0] for item in selected_items)
    total_points = INITIAL_POINTS + sum(ITEMS[item][1] for item in selected_items)

    if (total_weight <= MAX_CELLS and
            total_points > MIN_POINTS and
            all(item in selected_items for item in REQUIRED_ITEMS)):
        validCombinations.append((selected_items.copy(), total_points))

    for i in range(start_index, len(item_keys)):
        selected_items.append(item_keys[i])
        choose_items(selected_items, item_keys, i + 1)
        selected_items.pop()

validCombinations = []
item_keys = list(ITEMS.keys())

choose_items([], item_keys, 0)

with open("validCombinations.txt", "w") as file:
    file.write("Found combination:\n")
    for combo, points in validCombinations:
        file.write(f"Combination: {combo}, Survival points: {points}\n")

    inventory = [[' ' for _ in range(3)] for _ in range(3)]
    index = 0

    for i in range(3): 
        for j in range(3): 
            if index < len(combo):
                item = combo[index]
                size = ITEMS[item][0]

                if (j + size <= 3 and
                        all(inventory[i][j + s] == ' ' for s in range(size))):
                    for s in range(size):
                        inventory[i][j + s] = item  
                    index += 1  
                    j += size - 1

    for row in inventory:
        file.write(f"[{' ] [ '.join(row)}]\n")

print("Результаты записаны в файл validCombinations.txt.")