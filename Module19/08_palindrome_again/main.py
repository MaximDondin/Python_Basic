text = input('Введите строку: ')

def number_of_characters(text):
    repeat = {}
    for symbol in text:
        if symbol in repeat:
            repeat[symbol] += 1
        else:
            repeat[symbol] = 1
    return repeat

def check(repeat):
    count = 0
    for symbol in repeat:
        if repeat[symbol] % 2 != 0:
            count += 1
            if count >= 2:
                print('Нельзя сделать палиндромом')
                break
    else:
        print('Можно сделать палиндромом')

check(number_of_characters(text))
