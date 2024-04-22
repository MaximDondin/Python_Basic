violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

sequence_number = [
    'первой', 'второй', 'третьей', 'четвёртой',
    'пятой', 'шестой', 'седьмой', 'восьмой', 'девятой'
]

count = 0
volume = int(input('Сколько песен выбрать? '))
if 1 > volume:
    print('Ошибка. Кол-во песен не должно быть меньше 1')
elif 9 <= volume:
    print('Ошибка. В списке нет столько песен')
else:
    for i_number in range(volume):
        print(f'Название {sequence_number[i_number]} песни:', end = ' ')
        name = input()
        count += violator_songs.get(name, 0)
    print(f'\nОбщее время звучания песен: {round(count, 2)}')