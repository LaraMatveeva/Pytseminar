# Задача 1.
# Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

number_N = int(input('Введите количество элементов в массиве N '))
new_list = []
for i in range(number_N):
    num = int(input('Введите элемент списка '))
    new_list.append(num)
number_X = int(input('Введите число X '))
count = 0
for i in range(number_N):
    if new_list[i] == number_X:
        count += 1
print((f'-> {count}'))