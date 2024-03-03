videocard_list = []
new_videocard_list = []
max_generation = 0
volume = int(input('Кол-во видеокарт: '))

for index in range(volume):
    print(index + 1, 'Видеокарта:', end = ' ')
    videocard_list.append(int(input()))
    if max_generation < videocard_list[index]:
        max_generation = videocard_list[index]

for number in videocard_list:
    if number != max_generation:
        new_videocard_list.append(number)

print('\nСтарый список видеокарт:', videocard_list)
print('Новый список видеокарт:', new_videocard_list)