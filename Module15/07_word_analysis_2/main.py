word = input('Введите слово: ')
revers = ''

for index in range(len(word)):
    revers += word[len(word) - index - 1]

print('Результат:', revers)

if word == revers:
    print('\nСлово является палиндромом')
else:
    print('\nСлово не является палиндромом')