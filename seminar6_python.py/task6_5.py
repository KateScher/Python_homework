# Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.
# ***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

num = int(input("Введите число: ")) 
revr_num = 0    # начальное значение равно 0. Здесь будет указано число наоборот
def recur_reverse(num): 
    global revr_num   # можно использовать вне функции 
    if (num > 0): 
        Reminder = num % 10 
        revr_num = (revr_num * 10) + Reminder 
        recur_reverse(num // 10) 
    return revr_num 
 
 
revr_num = recur_reverse(num) 
print("%d" % revr_num)



