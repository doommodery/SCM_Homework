import math

radius = float(input("Введите радиус окружности: "))
angle_degrees = float(input("Введите угол в градусах: "))

angle_radians = math.radians(angle_degrees)

x = radius * math.cos(angle_radians)
y = radius * math.sin(angle_radians)

print(f"Координаты точки на окружности: ({x}, {y})")