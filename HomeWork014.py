# Задача №14: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal = int(input("Введите число: "))
print(f'{decimal} -> {bin(decimal)[2:]}')