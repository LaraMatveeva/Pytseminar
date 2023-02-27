# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя

# def main_menu(numb):
# if numb == 1:
# all_contacts()
# elif numb == 2:
# find_contact(name)
# elif numb == 3:
# add_contact(data)

# numb = int(input('Введите 1 - для печати всего справочника; 2 - для поиска контакта; 3 - для записи контакта'))
# main_menu(numb)

# print('1 - вывести все контакты \n ')
# print('2 - поиск контакта\n ')
# print('3 -добавить контакт\n ')
# print('4 - выход\n ')

# file_path = 'phone_book.txt'

# def tasks(task):
# if task == 4: print('до свидания')
# else:
# match task:
# case 1: # вывести все контакты
# with open(file_path, 'r', encoding='utf8') as open_book:
# for line in open_book:
# print(line)
# tasks(int(input('введите номер залачи от 1 до 4:')))
# case 2: # поиск контактов
# with open(file_path, 'r', encoding='utf8') as open_book:
# seach_param = input('Введите параметр для поиска: ' )
# for line in open_book:
# if seach_param in line:
# print(line)
# tasks(int(input('введите номер залачи от 1 до 4:')))

# case 3: # добавить контакт
# with open(file_path, 'a', encoding='utf8') as open_book:
# add_n1 = input('Введите фамилию: ' )
