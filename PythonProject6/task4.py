students = ["Олег", "Марія", "Іван", "Анна", "Петро", "Олена", "Максим", "Вікторія"]

search_name = input("Введіть ім'я студента для пошуку: ").lower()
is_found = False

for i in range(len(students)):
    if students[i].lower() == search_name:
        print(f"Студента знайдено! Його позиція у списку (індекс): {i}")
        is_found = True
        break

if not is_found:
    print("Студента не знайдено.")