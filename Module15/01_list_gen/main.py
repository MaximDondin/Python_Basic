number = int(input('Введите число: '))
uneven_numbers = []


for num in range(number):
    if num % 2 != 0:
        uneven_numbers.append(num)
print('Список из нечётных чисел от одного до N:', uneven_numbers)