def crypto(information):
    return calculation(information)

def calculation(data):
    result = []
    if isinstance(data, dict):
        data = data.values()
    for index, value in enumerate(data):
        if is_prime(index):
            result.append(value)
    return result

def is_prime(numb):
    if numb == 1:
        return False
    elif numb % 2 == 0:
        return numb == 2
    number_check = 3
    while number_check * number_check <= numb and numb % number_check != 0:
        number_check += 2
    return number_check * number_check > numb

print(crypto('О Дивный Новый мир!'))
print(crypto([100, 200, 300, 'буква', 0, 2, 'а']))
print(crypto({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))