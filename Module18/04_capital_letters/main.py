text = input('Введите строку: ').split()

print('\nРезультат:', end = ' ')
for word in text:
    print(word.title(), end = ' ')