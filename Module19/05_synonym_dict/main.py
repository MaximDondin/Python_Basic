sequence_number = [
    'Первая', 'Вторая', 'Третья', 'Четвёртая',
    'Пятая', 'Шестая', 'Седьмая', 'Восьмая', 'Девятая'
]
def search():
    new_word = input('\nВведите слово: ').lower()
    for key, count in synonyms.items():
        if new_word in key:
            print('Синоним:', count.title())
            break
        elif new_word in count:
            print('Синоним:', key.title())
            break
    else:
        print('Такого слова в словаре нет.')
        search()

synonyms = {}
numb = int(input('Введите количество пар слов: '))
for i_numb in range(numb):
    print(f'{sequence_number[i_numb]} пара:', end = ' ')
    words = input('').lower().replace('-', ' ').split()
    synonyms[words[0]] = words[1]
print(synonyms)
if numb > 0:
    search()
