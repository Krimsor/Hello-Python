# Задача №5: Реализуйте алгоритм перемешивания списка.

import random
lst =[random.randint(0,10) for i in range(random.randint(5,20))]
print(f"Список:\n{lst}")
random.shuffle(lst)
print(f"Перемешанный список:\n{lst}")