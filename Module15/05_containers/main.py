volume = int(input('Количество контейнеров: '))
warehouse = []
new_number = 0

for numb in range(volume):
    while True:
        massa = int(input('Введите вес контейнера: '))
        if massa <= 200:
            warehouse.append(massa)
            break
        else:
            print('\nОшибка! Масса не должна превышать 200')


while True:
    print('\nВведите вес нового контейнера:', end=' ')
    new_massa = int(input())
    if new_massa <= 200:
        break
    else:
        print('Ошибка! Масса не должна превышать 200')

for index in range(len(warehouse)):
    if warehouse[index] < new_massa:
        new_number = index + 1
        break
    elif warehouse[index] == new_massa:
        new_number = index + 2
    else:
        new_number = len(warehouse) + 1
print('\nНомер, который получит новый контейнер:', new_number)