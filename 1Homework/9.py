import math

bound = float(input("Введите границу интервала: "))


probability = 0.5 * (math.erf(bound/math.sqrt(2)) - math.erf(-bound/math.sqrt(2)))

print(f"Вероятность попадания в интервал [{-bound}, {bound}]: {probability:.4f}")