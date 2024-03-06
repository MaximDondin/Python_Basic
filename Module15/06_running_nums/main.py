import random

step = int(input('Сдвиг: '))
start_list = []
new_list = []

size = int(input('Введите кол-во элементов в списке: '))

for _ in range(size):
    start_list.append(random.randint(1, 9))

for index in range(size):
    if step > size:
        step -= size * (step // size)
    new_list.append(start_list[index - step])

print('Изначальный список:\t', start_list)
print('Сдвинутый список:\t', new_list)
