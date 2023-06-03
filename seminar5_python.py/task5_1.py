# Найти число Фибоначчи:
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
# Задание необходимо решать через рекурсию
def fib(count):
    if count == 1: return 0
    elif count == 2: return 1
    return fib(count - 2) + fib(count - 1)

# Обычное решение:
def F(n):
    if n in (1,2):
        return 1
    return F(n-1) + F(n-2)
print(F(7))


# Найти факториал:
def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

print(f(5))