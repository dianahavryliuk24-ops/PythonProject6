shopping_list = ["Хліб", "Молоко", "Яблука", "Сир", "М'ясо"]
print("Початковий список:", shopping_list)

shopping_list.append("Кава")
print("Після додавання 'Кава':", shopping_list)

shopping_list.remove("Молоко")
print("Після видалення 'Молоко':", shopping_list)

print("Кількість продуктів у списку:", len(shopping_list))

shopping_list.sort()
print("Список за алфавітом:", shopping_list)