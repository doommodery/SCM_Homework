import math

def solve_quadratic_equation():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2*a)
        print(f"Уравнение имеет один корень: x = {x}")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"Корни уравнения: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")

solve_quadratic_equation()