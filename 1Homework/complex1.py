import math

def calculate_temperature():
  
    angle = float(input("Введите угол:"))
    intensity = float(input("Введите интенсивность:"))
    pressure = float(input("Введите давление:"))

    angle_radians = math.radians(angle)
    angle_pow = math.radians(180)

    effective_angle = math.pi*math.sin(angle_radians) / angle_pow #math.sqrt(pressure / 101325))

    effective_pressure = math.exp(1)**(-pressure/101325)

    surface_intensity = intensity * effective_angle * math.log(effective_pressure + 1)

    effective_temperature = surface_intensity

    if effective_temperature > 0: 

        print('Эффективная температура на поверхности:',effective_temperature,"На планете может существовать вода в жидком состоянии.")

    else:

        print('Эффективная температура на поверхности:',effective_temperature,"Жидкой воды на планете не существует.")

calculate_temperature()