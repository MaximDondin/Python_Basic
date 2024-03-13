numb_list = []
new_list = []
list1 = []

size = int(input('Количество чисел: '))
for _ in range(size):
    number = int(input('Число: '))
    numb_list.append(number)
list1 = numb_list.copy()
list1.reverse()
print('Последовательность:', numb_list)
for _ in range(len(numb_list)):
    if numb_list != list1:
        new_list.append(numb_list[0])
        numb_list.remove(numb_list[0])
        list1 = numb_list.copy()
        list1.reverse()
    else:
        break

if len(new_list) == 0:
    print('Последовательность симметричная')
else:
    print('Нужно приписать чисел:', len(new_list))
    new_list.reverse()
    print('Сами числа:', new_list)