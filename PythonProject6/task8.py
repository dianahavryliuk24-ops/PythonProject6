products = [
    ("Ноутбук", 25000),
    ("Мишка", 800),
    ("Клавіатура", 1500),
    ("Монітор", 7000),
    ("Навушники", 2200)
]

print("--- Всі товари ---")
for product in products:
    print(f"{product[0]} - {product[1]} грн")

max_price = 0
most_expensive_product = ""

for product in products:
    name, price = product
    if price > max_price:
        max_price = price
        most_expensive_product = name
print(f"\nНайдорожчий товар: {most_expensive_product} ({max_price} грн)")

total_sum = 0
for product in products:
    total_sum += product[1]
print(f"Загальна вартість усіх товарів: {total_sum} грн")

print("\nТовари, дорожчі за 2000 грн:")
for product in products:
    if product[1] > 2000:
        print(f"- {product[0]} ({product[1]} грн)")