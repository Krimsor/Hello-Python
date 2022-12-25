# Здача №18 Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# lst1 = []
# [lst1.append(i) for i in lst if i not in lst1]
# print(f'Список из неповторяющихся элементов: {lst1}')


from collections import Counter

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")

counter = Counter(lst)

lst1 = [elem for elem, n in counter.items() if n == 1]
print(f'Список из неповторяющихся элементов: {lst1}')
