# Задача 39. Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива.
# Ввод: 7 
#       3 1 3 4 2 4 12
#       6
#       4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод: 3 3 2 12

def common_member(a, b):   
    a_set = set(a)
    b_set = set(b)
     
    # check length
    if len(a_set.intersection(b_set)) > 0:
        return(a_set.difference(b_set)) 
    else:
        return("no common elements")
     
  
a = list(map(int, input().split())) 
print(a)

b = list(map(int, input().split())) 
print(b)

print(common_member(a, b))