# Задача №43. Решение в группах Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые два элемента, равные друг другу 
# образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа 
# списка находятся на разных строках.
# Ввод:  1 2 3 2 3  Вывод:  2

# A = list(map(int, input().split()))
# n = len(A)
# c = 0
# for i in range(n):
#   for j in range(n):
#     if i - j > 0 and A[i] == A[j]:
#       c += 1 
# print("count:", c)


a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)