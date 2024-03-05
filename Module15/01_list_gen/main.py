while True:
    number = int(input('Введите число: '))
    if number > 0:
        break
    print('Введите число больше 0\n')
uneven_numbers = []

for num in range(1, number + 1):
    if num % 2 != 0:
        uneven_numbers.append(num)
print('Список из нечётных чисел от одного до N:', uneven_numbers)