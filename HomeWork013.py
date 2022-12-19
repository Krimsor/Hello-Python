# Задача №13: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

float_array = [1.1, 1.2, 3.1, 5, 10.01]
float_array1 = []
for i in range(len(float_array)):
    if float_array[i] % 1 != 0:
        float_array1.append(float_array[i])
float_array2 = [round(float_array1[i] % 1, 2)
                for i in range(len(float_array1))]

print(f'{float_array} -> {max(float_array2) - min(float_array2)}')