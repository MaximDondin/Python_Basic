count = 0
flag = False
while True:
    password = input('Придумайте пароль: ')
    if sum(map(str.isnumeric, password)) >= 3 and sum(map(str.isupper, password)) >= 1 and len(password) >= 8:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')