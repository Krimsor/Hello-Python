# Задача №11: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list =[random.randint(0,10) for i in range(random.randint(5,20))]

summ = 0
for i in range(len(list)):
    if i % 2 == 1:
        summ += list[i]       
print(f"{list} -> сумма элементов на нечётных позициях: {summ}")