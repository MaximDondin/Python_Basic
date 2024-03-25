import string

text = input('Введите текст: ')
vowel_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
result = []

for letter in range(len(text)):
    for vowel in vowel_letters:
        if text[letter] == vowel or text[letter] == string.capwords(vowel):
            result.append(text[letter])
print('Список гласных букв:', result)
print('Длина списка:', len(result))
