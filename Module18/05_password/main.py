count = 0
flag = False
while True:
    password = input('Придумайте пароль: ')
    if len(password) >= 8:
        for i_letter in range(len(password)):
            if password[i_letter] == password[i_letter].upper() and not password[i_letter].isnumeric():
                flag = True
            if password[i_letter].isnumeric():
                count += 1
        if count >= 3 and flag:
            print('Это надёжный пароль!')
            break
    print('Пароль ненадёжный. Попробуйте ещё раз.')

# TODO: решение рабочее, но как избавиться от флага?
