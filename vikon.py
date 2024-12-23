items = [
    ('r', 3, 25),  # Винтовка
    ('p', 2, 15),  # Пистолет
    ('a', 2, 15),  # Боекомплект
    ('m', 2, 20),  # Аптечка
    ('i', 1, 5),   # Ингалятор (обязателен)
    ('k', 1, 15),  # Нож
    ('x', 3, 20),  # Топор
    ('t', 1, 25),  # Оберег
    ('f', 1, 15),  # Фляжка
    ('d', 1, 10),  # Антидот (обязателен)
    ('s', 2, 20),  # Еда
    ('c', 2, 20),  # Арбалет
]

rows = 3
cols = 3
total_cells = rows * cols  

required_items = {'i', 'd'}  

def optimize_inventory(items, total_cells, required_items):
    inventory = [[' ' for _ in range(cols)] for _ in range(rows)]  
    available_cells = total_cells
    total_survival_points = 0
    selected_items = []

    for item, size, points in items:
        if item in required_items:
            if size <= available_cells:
                selected_items.append((item, size, points))
                total_survival_points += points
                available_cells -= size
                required_items.remove(item)  
            else:
                print(f"Ошибка: Недостаточно места для обязательного предмета {item}.")
                return None, None

    items_sorted = sorted([(item, size, points) for item, size, points in items if item not in [i[0] for i in selected_items]],
                          key=lambda x: x[2], reverse=True)

    placed_items = set()  
    for item, size, points in selected_items + items_sorted:
        if item in placed_items:
            continue  

        placed = False
        for row in range(rows):
            for col in range(cols):
                if inventory[row][col] == ' ':
                    can_place = True
                    for i in range(size):
                        r = row + i // cols
                        c = col + i % cols
                        if r >= rows or c >= cols or inventory[r][c] != ' ':
                            can_place = False
                            break

                    if can_place:
                        for i in range(size):
                            r = row + i // cols
                            c = col + i % cols
                            inventory[r][c] = item
                        total_survival_points += points
                        placed_items.add(item) 
                        placed = True
                        break
            if placed:
                break

    return inventory, total_survival_points

inventory, total_survival_points = optimize_inventory(items, total_cells, required_items)

if inventory:
    for row in inventory:
        print(row)
    print(f"Итоговые очки выживания: {total_survival_points}")
