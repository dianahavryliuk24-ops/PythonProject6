grades = [10, 8, 12, 11, 4, 9, 7, 3, 10, 11]

print("Усі оцінки:", grades)
print("Найвища оцінка:", max(grades))
print("Найнижча оцінка:", min(grades))

average = sum(grades) / len(grades)
print(f"Середній бал: {average}")

high_grades_count = 0
for grade in grades:
    if grade >= 10:
        high_grades_count += 1
print("Кількість оцінок (>= 10):", high_grades_count)

print("Оцінки, нижчі за 4:")
for grade in grades:
    if grade < 4:
        print(grade)