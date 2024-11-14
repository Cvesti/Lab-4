#Предметы и их характеристики
items = {
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

max_cells = 9       
min_points = 0      
initial_points = 10 
required_items = ['i']  

def choose_items(selected_items, item_keys, start_index):
    total_weight = sum(items[item][0] for item in selected_items)
    total_points = initial_points + sum(items[item][1] for item in selected_items)


    if total_weight <= max_cells and total_points > min_points and all(item in selected_items for item in required_items):
        global best_combination, best_points
        if total_points > best_points:
            best_points = total_points
            best_combination = selected_items.copy()

    for i in range(start_index, len(item_keys)):
        selected_items.append(item_keys[i])
        choose_items(selected_items, item_keys, i + 1)
        selected_items.pop()

best_combination = []
best_points = -float('inf')

item_keys = list(items.keys())
choose_items([], item_keys, 0)

inventory = [[' ' for _ in range(3)] for _ in range(3)]
item_list = list(best_combination)

index = 0
for i in range(3):
    for j in range(3): 
        if index < len(item_list):
            item = item_list[index]
            size = items[item][0]

            if j + size <= 3 and all(inventory[i][j + s] == ' ' for s in range(size)):
                for s in range(size):
                    inventory[i][j + s] = item
                
                index += 1
                j += size - 1

# Вывод результата
for row in inventory:
    print(f"[{' ] ['.join(row)}]")
    
print(f"Итоговые очки выживания: {best_points}")