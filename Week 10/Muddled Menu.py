"""Muddled Menu"""
def manage_menu():
    """Management"""
    menu = []

    while True:
        line = input().strip()
        if line == "DONE":
            break
        if line == "CLOSED":
            menu.clear()
            break
        if line == "SOMETHING'S WRONG":
            menu.clear()
            continue
        if line.startswith("Can't do: "):
            dish_name = line[len("Can't do: "):].strip()
            if dish_name in menu:
                menu.remove(dish_name)
            continue
        parts = line.rsplit(" #", 1)
        if len(parts) != 2:
            continue
        dish_name, course_number = parts[0].strip(), parts[1].strip()
        if course_number == "N":
            menu.append(dish_name)
        else:
            course_index = int(course_number) - 1
            if 0 <= course_index <= len(menu):
                menu.insert(course_index, dish_name)
    print(f"Full Course: {menu} Reversed: {menu[::-1]}")
manage_menu()
