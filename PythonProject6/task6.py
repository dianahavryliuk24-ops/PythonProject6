point_a = (2, 5)
point_b = (8, 3)
point_c = (4, 9)

print(f"Координати точки A: {point_a}")
print(f"Координати точки B: {point_b}")
print(f"Координати точки C: {point_c}")

x1, y1 = point_a
x2, y2 = point_b
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f"Відстань між точками A та B: {distance}")

max_y_point = point_a

if point_b[1] > max_y_point[1]:
    max_y_point = point_b
if point_c[1] > max_y_point[1]:
    max_y_point = point_c

print("Точка з найбільшою Y координатою:", max_y_point)