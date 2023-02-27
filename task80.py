# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя
# 5. Изменение контакта
# 6. Удаление контакта

def main_menu(number):
    if number == 1:
        print('Полный список контактов\n')
        with open(file_path, 'r', encoding='utf8') as file_manager:
            for line in file_manager:
                print(line)
    elif number == 2:
        print('Поиск контакта\n')
        with open(file_path, 'r', encoding='utf8') as file_manager:
            name_contact = input('Введите имя или фамилию контакта  ')
            marker = False
            for line in file_manager:
                if name_contact in line:
                   print(line)
                   marker = True
            if marker == False:
                print('\n Такого контакта не существует') 

    elif number == 3:
        print('Добавление нового контакта')
        with open(file_path, 'a', encoding='utf8') as file_manager:
            name_contact = input('\nВведите фамилию контакта  ')\
                           + ' ' + input('\nВведите имя контакта  ')\
                           + ' ' + input('\nВведите номер телефона  ')
            file_manager.write('\n')
            file_manager.write(name_contact)

    elif number == 4:
        print('Изменение контакта')  
        with open(file_path, 'r', encoding='utf8') as file_manager:
            copy_book = file_manager.readlines()
            name_contact = input('Введите имя или фамилию контакта  ')
            for i in range(len(copy_book)):
                if name_contact in copy_book[i]:
                    print(copy_book[i])
                    copy_book[i] = input('\n Введите новые данные:\n фамилию контакта  ')\
                           + ' ' + input('\nВведите имя контакта  ')\
                           + ' ' + input('\nВведите номер телефона  ') + '\n'
        with open(file_path, 'w', encoding='utf8') as file_manager:
            file_manager.writelines(copy_book)
                
                      
    elif number == 5:
        print('Удаление контакта')  
        with open(file_path, 'r', encoding='utf8') as file_manager:
            copy_book = file_manager.readlines()
            name_contact = input('Введите имя или фамилию контакта  ')
            for i in range(len(copy_book)):
                if name_contact in copy_book[i]:
                    print(copy_book[i])
                    del copy_book[i]
                    break
        with open(file_path, 'w', encoding='utf8') as file_manager:
            file_manager.writelines(copy_book)
    
    elif number == 6:
        print('Выход') 
      

file_path = 'phone_book.txt'
number = 0
while number != 6:
     number = int(input('Введите\n1 - Вывод контактов\n'
                    '2 - Поиск контакта\n'
                    '3 - Добавление контакта\n'
                    '4 - Изменение контакта\n'
                    '5 - Удаление контакта\n'
                    '6 - Выход из меню\n'))
     main_menu(number)