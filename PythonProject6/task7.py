numbers = [4, 7, 2, 4, 9, 7, 1, 2, 8, 9]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Початковий список:", numbers)
print("Список унікальних чисел:", unique_numbers)