numbers = [12, 45, 2, 7, 99, 14, 26, 33, 8, 11, 40, 5, 17, 22, 50]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Парні числа:", even_numbers)
print("Кількість парних:", len(even_numbers))

print("Непарні числа:", odd_numbers)
print("Кількість непарних:", len(odd_numbers))

print("Сума всіх парних чисел:", sum(even_numbers))