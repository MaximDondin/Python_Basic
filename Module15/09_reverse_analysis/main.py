import random

size = int(input('Введите размер списка: '))
numbers_list = []
count = 0

for _ in range(size):
    numbers_list.append(random.randint(0,9))

print('Исходный список\t', numbers_list)
print('Чётные цифры в обратном порядке: [ ', end = '')
#numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
for i in range(len(numbers_list)):
    if numbers_list[len(numbers_list) - i - 1] % 2 == 0:
        print(numbers_list[len(numbers_list) - i - 1], end = ' ')
print(']')
# print('Чётные цифры в обратном порядке:', end = ' ')
# for i in range(len(numbers_list)):
#     print(numbers_list[len(numbers_list) - i - 1], end = ' ')