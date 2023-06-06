# Задача N 45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284

# def find_div_sum(num: int) -> int:
#     div_sum = 0
#     for i in range(1, num//2+1):
#         if num % i == 0:
#             div_sum += i
#     return div_sum


# k = int(input())
# result = []
# for i in range(k):
#     second = find_div_sum(i)
#     first = find_div_sum(second)
#     if i == first and i != second:
#         if (second, i) not in result:
#             result.append((i, second))
# print(result)


# пример идеального решения:
n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_1.append(tuple([i, summa]))
for i in range(len(list_1)):
    for j in range(i, len(list_1)):
        if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
            print(*list_1[i])


def s(n):
    list1 = [i for i in range(1,n) if n % i == 0]
    sum = 0
    for i in list1:
        sum += i
        # print(i)
    return sum    
    
k = 300
for i in range(1,k):
    for j in range(1,k):
        if s(i) == j and s(j) == i and i != j:
            print(f"{i} и {j}")