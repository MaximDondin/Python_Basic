def new_zip(data_1, data_2):
    data_1, data_2 = check(data_1), check(data_2)
    # length = 0
    # if len(data_1) > len(data_2):
    #     length = len(data_2)
    # else:
    #     length = len(data_1)
    print('Результат:')
    print(tuple([data_1[0], data_2[0]]) for i in range(1))  #для вывода строки <generator object new_zip.<locals>.<genexpr> at 0x00000158742E5210>
    print(* [tuple([data_1[i], data_2[i]])
             for i in range(len(data_2) if len(data_1) > len(data_2) else len(data_1))],
          sep = '\n')

def check(data):
    if type(data) == dict:
        data = [numb for numb in data.keys()]
    elif type(data) == set:
        data = list(data)
    return data

data_1 = input('Строка: ')
data_2 = tuple(int(numb) for numb in input('Кортеж чисел: ').split(','))

#data_2 = {15: 20, 17: 52, 19: 88}
#data_2 = [11, 19, 25, 44]
#data_2 = {1, 3, 8, 16, 50}  #не получается сохранить такой же порядок как в исходнике!

new_zip(data_1, data_2)