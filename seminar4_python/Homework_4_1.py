# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n1 = int(input('Введите количество элементов 1-го набора чисел: '))
n2 = int(input('Введите количество элементов 2-го набора чисел: '))
arr1 = []
arr2 = []
for i in range(n1):
    arr1.append(int(input('Введите элемент 1-го массива: ')))
for j in range(n2):
    arr2.append(int(input('Введите элемент 2-го массива: ')))
arr3 = []
for i in arr1:
    if i in arr2 and i not in arr3:
            arr3.append(i)
arr3.sort()
print(*arr3, sep=" ")
    
        
        
