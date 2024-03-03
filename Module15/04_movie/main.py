films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favourite_films = []

add_film = int(input('Сколько фильмов хотите добавить? '))
for index in range(add_film):
    name = input('Введите название фильма: ')
    for film in films:
        if film == name:
            favourite_films.append(name)
            break
    else:
        print('Ошибка: фильма', name, 'у нас нет :(')

print('\nВаш список любимых фильмов:', end = ' ')
for name in favourite_films:
    print(name, end = ' ')