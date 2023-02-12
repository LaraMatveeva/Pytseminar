# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9

quantity_n = 1
while quantity_n < 3:
    quantity_n = int(input('Введите количество кустов на грядке не менее трех '))
bushes = list()
print('Введите количество ягод на кусте  ')
for i in range(quantity_n):
    num = int(input(''))
    bushes.append(num)
    i += 1
berries = list()
for i in range(quantity_n):
    sum = 0
    if i == (quantity_n - 1):
        sum = bushes[i-1] + bushes[i] + bushes[0]  
    else:
        sum = bushes[i-1] + bushes[i] + bushes[i+1]
    berries.append(sum)
    i += 1
max = 0
for i in range(quantity_n):
    if berries[i] > max:
        max = berries[i]
    i += 1
print(max)
