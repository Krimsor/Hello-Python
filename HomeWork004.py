# Задача №4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

NumberQuarter = int(input('Введите номер четверти: '))

if NumberQuarter == 1:
    print(f'1 -> x > 0; y > 0')
elif NumberQuarter == 2:
    print(f'2 -> x < 0; y > 0')
elif NumberQuarter == 3:
    print(f'3 -> x < 0; y < 0')
elif NumberQuarter == 4:
    print(f'4 -> x > 0; y < 0')
else:
    print(f'Такой четверти нет!')
