# Здача №16 Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = int(input('Введите число для заданной точности числа "Пи": ')) # количество знаков после запятой
print(f'$d = {d}, π = {round(pi, d)}')