length = int(input('Введите длину списка: '))
result = [(numb % 5 if numb % 2 != 0 else 1) for numb in range(length)]
print('Результат:', result)