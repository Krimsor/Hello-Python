# Задача №2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    list = []
    for i in range(x):
        list.append(input(f"Введите значение {xyz[i]}: "))
    return list


def Predicate(x):
    leftsite = not (x[0] or x[1] or x[2])
    rightsite = not x[0] and not x[1] and not x[2]
    result = leftsite == rightsite
    return result


statement = inputNumbers(3)

if Predicate(statement) == True:
    print(f"True")
else:
    print(f"False")


#not(x or y or z) == not x or not y or not z  
# xyz = ['X', 'Y', 'Z']
# print("x y z")
# for x in range(0, 2):
# 	for y in range(0, 2):
# 		for z in range(0, 2):
# 			result = x == ((y and z) <= x)
# 			print(x, y, z, result)