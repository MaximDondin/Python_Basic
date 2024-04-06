first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
count = 0

if first_str == second_str:
    print('Строки равны')
elif len(second_str) > len(first_str):
    print('Вторая строка не может быть больше первой!')
else:
    for _ in range(len(second_str)):
        if second_str not in first_str:
            second_str = second_str[-1:] + second_str[:len(second_str) - 1]
            count += 1
        else:
            print('Первая строка получается из второй со сдвигом', count)
            break
    else:
        print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')