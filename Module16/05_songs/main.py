violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]]

numb = int(input('Сколько песен выбрать? '))
if numb <= 0:
    print('Ошибка ввода')
else:
    new_list = []
    for i_count in range(numb):
        print('Название', i_count + 1, 'песни: ', end = '')
        song = input()
        flag = False
        for j_son in violator_songs:
            if song == j_son[0]:
                new_list.append(song)
                flag = True
        if flag == False:
            print('Такой песни нет')
    time = 0
    for i_song in new_list:
        for j_song in violator_songs:
            if i_song == j_song[0]:
                time += j_song[1]
    print('Общее время звучания песен:', round(time, 2), 'минуты')