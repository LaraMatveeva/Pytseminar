# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

quantity_n = int(input('Введите количество элементов первого множества n '))
quantity_m = int(input('Введите количество элементов второго множества m '))

list_n = []
list_m = []
print('Введите элементы первого множества')
for i in range(quantity_n):
    num = int(input(''))
    list_n.append(num)
    i += 1

print('Введите элементы второго множества')
for i in range(quantity_m):
    num = int(input(''))
    list_m.append(num)
    i += 1

set_n = set(list_n)
set_m = set(list_m)
new_set = set_n.intersection(set_m)
print(*(sorted(list(new_set))))