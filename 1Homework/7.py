import math

vector1_x = float(input("Введите x-координату первого вектора: "))
vector1_y = float(input("Введите y-координату первого вектора: "))

vector2_x = float(input("Введите x-координату второго вектора: "))
vector2_y = float(input("Введите y-координату второго вектора: "))

dot_product = vector1_x * vector2_x + vector1_y * vector2_y

vector1_magnitude = math.sqrt(vector1_x**2 + vector1_y**2)
vector2_magnitude = math.sqrt(vector2_x**2 + vector2_y**2)

angle = math.acos(dot_product / (vector1_magnitude * vector2_magnitude))

angle_degrees = math.degrees(angle)

print(f"Угол между векторами: {angle_degrees:.2f} градусов")