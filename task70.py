# def find_farthest_orbit(list_of_orbits: list([tuple])) -> tuple:
#     func_list_orbits = list_of_orbits.copy()
#     func_list_orbits = list(filter(lambda orbits: orbits[0] != orbits[1], func_list_orbits))
#     s_orbits = tuple(map(lambda orbits: orbits[0]*orbits[1], func_list_orbits))
#     max_orbits = max(s_orbits)
#     index_max_s = s_orbits.index(max_orbits)
#     return func_list_orbits[index_max_s]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))



# def find_farthest_orbit(list_of_orbits: list([tuple])):
    # func_list_orbits = list_of_orbits.copy()
    # func_list_orbits = list(filter(lambda orbits: orbits[0] != orbits[1], func_list_orbits))
    # s_orbits = tuple(map(lambda orbits: orbits[0]*orbits[1], func_list_orbits))
    # max_orbits = max(s_orbits)
    # index_max_s = s_orbits.index(max_orbits)
    # return func_list_orbits[index_max_s]

    # s_orbit = {(orbita[0]*orbita[1]): orbita for orbita in list_of_orbits if orbita[0] != orbita[1]}
    # return s_orbit[max(s_orbit)]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# Напишите функцию same_by(characteristic, objects), 
# которая проверяет, все ли объекты имеют одинаковое значение некоторой 
# характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     return len(set(map(characteristic, objects))) == 1

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

def same_by(characteristic, objects):
    if objects:
        return len(set(map(characteristic, objects))) == 1
    return True

values = []
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')