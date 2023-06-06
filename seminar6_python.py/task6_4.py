# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод: 5         Ввод: 5
# 1 2 3 4 5       1 5 1 5 1
# Вывод:         Вывод:
# 0                 2

# def revers(n):
#     if n > 0:
#         print(n)
#         revers(n-1)
# n = int(input('Введите число:  '))
# revers(n)


import random
list1 = []
for i in range(1,10):
    i = random.randint(1,10)
    list1.append(i)
print(list1)
count = 0
for i in range(1, len(list1)-1):
    if list1[i-1] < list1[i] > list1[i+1]:
        count += 1
print(count)



# import random
# list1 = []
# for i in range(1,10):
#     i = random.randint(1,10)
#     list1.append(i)
# print(list1)
# count = 0
# for i in range(1, len(list1)-1):
#     if list1[i-1] < list1[i] > list1[i+1]:
#         count += 1
# print(count)