# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение

# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1 list cpmprehension.

print('Введите целые числа через пробел: ')

print(*[int(i) ** 3 for i in input().split()])  # куб числа

# 2 map. список из неповторяющеейся элементов (задача)

lst = [x for x in range(1, 20)]

lst = list(map(lambda x: x + 10, lst))

print(lst)

# 3 lambda


def select(fun, col):
    return [fun(x) for x in col]


def where(fun, col):
    return [x for x in col if fun(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)  # список четных чисел
res = select(lambda x: (x, x ** 2), res)  # кортежы - квадрат числа
print(*res)  # * - распаковка

# 4 filter

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))

print(res)

# 5 zip

obj = ['obj1', 'obj2', 'obj3', 'obj4', 'obj5',]
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(obj, ids, salary))
print(data)

# 6 enumerate

city = ['Moscow', 'Khabarovsk', 'Vladivostok']

data = list(enumerate(city))
print(data)

# city = ['Moscow', 'Khabarovsk', 'Vladivostok']

# for i, value in enumerate(city, 1): # индексы с '1' и в столбик списком.
#     print(i, value)
