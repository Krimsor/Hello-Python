# Задача №10: Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random
lst =[random.randint(0,10) for i in range(random.randint(5,20))]
print(f"Список:\n{lst}")
random.shuffle(lst)
print(f"Перемешанный список:\n{lst}")