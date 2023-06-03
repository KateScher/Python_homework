# Определить, является ли слово палиндромом.

def pal(word):
    if len(word) == 0: return ''
    c = word.pop(0)
    return pal(word) + c


word = 'око'
text = [item for item in word]
if word == pal(text): print('Да')
else: print('Нет')