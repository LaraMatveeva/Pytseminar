# Задача 1: Найдите сумму цифр трехзначного числа.
# # 123 -> 6 (1 + 2 + 3)
# # 100 -> 1 (1 + 0 + 0)

f = int(input('Введите трехзначное число -->'))
summa = f % 10 + f // 100 + ((f // 10) % 10)
print(f'Сумма цифр числа равна -->{summa} ({f // 100} + {(f // 10) % 10} + {f % 10})')
