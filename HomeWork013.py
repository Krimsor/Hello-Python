# Задача №13: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import numpy

random_float_array = numpy.random.uniform(low=0.1, high=10.9, size=(5))
print(random_float_array)

new_lst = [round(i%1,2) for i in random_float_array if i%1 != 0]
print(max(new_lst) - min(new_lst))