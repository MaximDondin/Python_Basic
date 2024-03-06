import random

size = int(input('Введите размер списка: '))
numbers_list = []

for _ in range(size):
    numbers_list.append(random.randint(0,9))
print('Исходный список\t', numbers_list)

for numb_i in range(size):
    for numb_j in range(numb_i + 1, size):
        if numbers_list[numb_i] > numbers_list[numb_j]:
            numbers_list[numb_i], numbers_list[numb_j] = numbers_list[numb_j], numbers_list[numb_i]
print('Отсортированный список\t', numbers_list)