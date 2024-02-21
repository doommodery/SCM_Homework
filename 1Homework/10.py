import math

def volume_n_sphere():
    n = float(input("Введите n:"))
    R = float(input("Введите R:"))

    if n < 0:
        raise ValueError("Размерность пространства должна быть неотрицательной.")

    volume = (math.pi ** (n / 2) * R ** n) / math.gamma((n / 2) + 1)

    print(volume)


volume_n_sphere()