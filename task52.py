# Задача 2
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# 2 2
# 4

def multi_summa(number_A, number_B):
    if number_B == 0:
        return number_A
    else:
        number_A += 1
        number_B -= 1
    return multi_summa(number_A, number_B)

number_A = int(input('Введите число A '))
number_B = int(input('Введите число B '))
print (f'A = {number_A}; B = {number_B} -> {multi_summa(number_A, number_B)} ')