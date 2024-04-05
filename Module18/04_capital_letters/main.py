text = input('Введите строку: ').split()

print('\nРезультат:', end = ' ')
for word in text:
    print(word.title(), end = ' ')

# TODO: как работает .title() и почему не нужен цикл?
