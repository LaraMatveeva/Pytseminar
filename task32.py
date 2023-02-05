# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

number_N = int(input('Введите количество элементов в массиве N '))
new_list = []
for i in range(number_N):
    num = int(input('Введите элемент списка '))
    new_list.append(num)
number_X = int(input('Введите число X '))

min = abs(number_X - new_list[0]) 
min_k = 0 
for i in range(1,number_N):
    if min > abs(number_X - new_list[i]):
        min = abs(number_X - new_list[i])
        min_k = i
print((f'-> {new_list[min_k]}'))