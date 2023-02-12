# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def multi_step(number_A, number_B, rez):
    if number_B == 0:
        return rez
    else:
        rez *= number_A 
        number_B -= 1
    return multi_step(number_A, number_B, rez)

number_A = int(input('Введите число A '))
number_B = int(input('Введите степень числа B '))
rez = 1
print (f'A = {number_A}; B = {number_B} -> {multi_step(number_A, number_B, rez)} ')