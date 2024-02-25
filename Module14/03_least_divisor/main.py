# TODO здесь писать код
def main():
    number = int(input('Введите натуральное число n > 1: '))
    if number <= 1:
        print('натуральное число должно быть n > 1 \nповторите попытку\n')
        main()
    else:
        print('\nНаименьший делитель, отличный от единицы:', min_divider(number))

def min_divider(number):
    divider = 0
    for numb in range(2, number + 1):
        if number % numb == 0:
            divider = numb
            break
    return divider

main()
