students = [
    ["Олександр", [10, 11, 9]],
    ["Марія", [12, 10, 12]],
    ["Іван", [7, 8, 9]]
]

while True:
    print("\n===== ЕЛЕКТРОННИЙ ЖУРНАЛ =====")
    print("1. Показати всіх студентів")
    print("2. Додати студента")
    print("3. Додати оцінку студенту")
    print("4. Переглянути оцінки студента")
    print("5. Показати середній бал студента")
    print("6. Видалити студента")
    print("0. Вихід")

    choice = input("Оберіть дію (0-6): ")

    if choice == "0":
        print("Роботу завершено.")
        break

    elif choice == "1":
        print("\n--- Список студентів ---")
        for student in students:
            print(f"{student[0]}: {student[1]}")

    elif choice == "2":
        name = input("Введіть ім'я нового студента: ")
        students.append([name, []])
        print(f"Студента {name} успішно додано!")

    elif choice == "3":
        name = input("Введіть ім'я студента: ")
        found = False
        for student in students:
            if student[0].lower() == name.lower():
                mark = int(input(f"Введіть нову оцінку для {student[0]}: "))
                student[1].append(mark)
                print("Оцінку додано!")
                found = True
                break
        if not found:
            print("Студента не знайдено.")

    elif choice == "4":
        name = input("Введіть ім'я студента: ")
        found = False
        for student in students:
            if student[0].lower() == name.lower():
                print(f"Оцінки {student[0]}: {student[1]}")
                found = True
                break
        if not found:
            print("Студента не знайдено.")

    elif choice == "5":
        name = input("Введіть ім'я студента: ")
        found = False
        for student in students:
            if student[0].lower() == name.lower():
                if len(student[1]) > 0:
                    avg = sum(student[1]) / len(student[1])
                    print(f"Середній бал {student[0]}: {avg:.1f}")
                else:
                    print("У студента ще немає оцінок.")
                found = True
                break
        if not found:
            print("Студента не знайдено.")

    elif choice == "6":
        name = input("Введіть ім'я студента для видалення: ")
        found = False
        for i in range(len(students)):
            if students[i][0].lower() == name.lower():
                removed = students.pop(i)
                print(f"Студента {removed[0]} видалено з журналу.")
                found = True
                break
        if not found:
            print("Студента не знайдено.")

    else:
        print("Невірний вибір. Спробуйте ще раз.")