def f(x):
    return x**2


def trapezoidal_integral(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    
    for i in range(1, n):
        integral += f(a + i*h)
    
    integral *= h
    return integral


a = float(input("Введите начало интервала: "))
b = float(input("Введите конец интервала: "))
n = int(input("Введите количество разбиений: "))


result = trapezoidal_integral(f, a, b, n)

print("Значение интеграла:", result)