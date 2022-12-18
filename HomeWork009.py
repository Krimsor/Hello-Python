# Задача №9: Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке (пример n=4, lst1=[4,-2,1,3] - список на основе n, а позиции элементов lst2=[3,1]).

from random import randint
numbers = []
for i in range(4):
    numbers.append(randint(-4, 4))
print(numbers)


def get_numbers(numbers):
    count = 0
    for element in numbers:
        count += 1
    return count


print('Количество элементов: ', get_numbers(numbers))

x = int(input('Введите первый элемент: '))
y = int(input('Введите второй элемент: '))

for i in range(len(numbers)):
    multiplication = numbers[x - 1] * numbers[y - 1]

print(f'Произведение элементов: {numbers[x - 1]} * {numbers[y - 1]} =', multiplication)
