# TODO здесь писать код
def main():
    number = int(input('Введите целое положительное число N: '))
    if number < 0:
        print('Неверный ввод! \nповторите попытку\n')
        main()
    else:
        print('\nСумма чисел:', summ_numb(number))
        print('Количество цифр в числе:', length_numb(number))
        print('Разность суммы и количества цифр:', summ_numb(number) - length_numb(number))

def summ_numb(number):
    last_num = 0
    summ = 0
    while number != 0:
        last_num = number % 10
        summ += last_num
        number //= 10
    return summ

def length_numb(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count

main()