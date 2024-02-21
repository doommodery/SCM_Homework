import math

def sqrt_newton_method(a, epsilon=1e-10):
    x = a
    while True:
        next_x = 0.5 * (x + a / x)
        if abs(x - next_x) < epsilon:
            break
        x = next_x
    return x

def main():
    a = float(input("Введите число для извлечения квадратного корня: "))
    
    my_sqrt = sqrt_newton_method(a)
    print(f"Квадратный корень из числа {a} (метод Ньютона): {my_sqrt}")
    
    math_sqrt = math.sqrt(a)
    print(f"Квадратный корень из числа {a} (стандартная функция sqrt): {math_sqrt}")
    
    difference = abs(my_sqrt - math_sqrt)
    print(f"Разница между результатами: {difference}")

if __name__ == "__main__":
    main()