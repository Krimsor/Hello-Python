# Задача №5. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите x1 = '))
y1 = int(input('Введите y1 = '))
x2 = int(input('Введите x2 = '))
y2 = int(input('Введите y2 = '))

A = x2 - x1
B = y2 - y1

from math import*

res = sqrt( A * A + B * B )
print(f'Длина отрезка: A ({x1},{y1}); B ({x2},{y2}) -> {round(res, 2)}')