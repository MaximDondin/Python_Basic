while True:
    password = input('Придумайте пароль: ')
    if (not password.islower()
            and sum(i_letter.isnumeric() for i_letter in password) >= 3
            and len(password) >= 8):
        print('\nЭто надёжный пароль!')
        break
    else:
        print('\nПароль ненадёжный. Попробуйте ещё раз.')