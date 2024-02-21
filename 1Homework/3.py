def f(x):
    return x**3 - x - 2

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Метод бисекции не применим на данном интервале!")
        return None

    while (b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

a = float(input("Введите начало интервала a: "))
b = float(input("Введите конец интервала b: "))
tol = float(input("Введите точность: "))

root = bisection_method(a, b, tol)

if root is not None:
    print(f"Корень уравнения на интервале [{a}, {b}]: {root}")