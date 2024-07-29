import random
def write_numb():
    summ_numb = 0
    try:
        with open('out_file.txt', 'w') as file:
            while summ_numb <= 777:
                my_numb = int(input('Введите число: '))
                summ_numb += my_numb
                rand_numb = random.randint(1, 13)
                if rand_numb == 5: # в rand_numb любое число появляется с вероятностью 1/13, я взял 5
                    raise Exception('Вас постигла неудача!')
                else:
                    file.write(str(my_numb) + '\n')
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
    except Exception as error:
        print(error)

write_numb()