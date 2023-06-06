# Задача на палиндром

# slovo = str(input())
# x = len(slovo)
# i = 0
# x = x - 1
# k = 0
# while x - i >= i:
#     if slovo[x - i] == slovo[i]:
#         i += 1
#     else:
#         k = 1
#         break
# if k == 1:
#   print("no")
# else:
#   print("yes")


#через рекурсию

# def poli(s):
#     if len(s) in [1,2]:
#         return s[0] == s[-1]
#     return s[0] == s[-1] and poli(s[1:len(s)-1])


# через рекурсию
# a = "abccba"
# print(poli(a))

def poli(s):
    if len(s) in [1,2]:
        return s[0] == s[-1]
    return s[0] == s[-1] and poli(s[1:-1])

a = "abba"
print(poli(a))