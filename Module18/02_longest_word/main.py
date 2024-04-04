text = input('Введите строку: ').split()
count = [0, 0]
for word in text:
    if len(word) > count[0]:
        count[0] = len(word)
        count[1] = word
print('Самое длинное слово:', count[1])
print('Длина этого слова:', count[0])