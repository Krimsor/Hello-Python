# Задача № 8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите x! = 0: '))
y = int(input('Введите y! = 0: '))

if x == 0 and y == 0:
    print('Значение условия НЕ верно!')
elif x > 0 and y > 0:
    print(f'x = {x}; y = {y} -> 1')
elif x < 0 and y > 0:
    print(f'x = {x}; y = {y} -> 2')
elif x < 0 and y < 0:
    print(f'x = {x}; y = {y} -> 3')
elif x > 0 and y < 0:
    print(f'x = {x}; y = {y} -> 4')
