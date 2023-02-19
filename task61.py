# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# number_A = int(input('Введите первый элемент арифм прогрессии A '))
# number_B = int(input('Введите число B - шаг  '))
# number_C = int(input('Введите число C - количество чисел прогрессии '))

# rezult = [int(input('num')) + int(input'step') for i in range(number_C + 1)]
# rezult = [item for item  in range(int(input('A->')), int(input('C->')), int(input('B->')))]
# rezult = [item for item  in range(number_A, number_C, number_B)]
# print (*rezult)
print (*([item for item  in range(int(input('A->')), int(input('C->')), int(input('B->')))]))