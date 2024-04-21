array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

def task_1():
    print('\nЭлементы, которые есть в каждом списке')
    print('Без использования множеств:', end=' ')
    for numb in array_1:
        if numb in (array_2 and array_3):
            print(numb, end=', ')
    print('\nС использования множеств:',
          sorted(set(array_1).intersection(set(array_2), set(array_3))))

def task_2():
    print('\nЭлементы из первого списка, которых нет во втором и третьем списках')
    print('Без использования множеств:', end=' ')
    for numb in array_1:
        if not numb in array_2 and not numb in array_3:
            print(numb, end=', ')
    print('\nС использования множеств:',
          sorted(set(array_1).difference(set(array_2), set(array_3))))

task_1()
task_2()