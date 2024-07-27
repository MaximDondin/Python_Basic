def writ_chat(path, name):
    while True:
        try:
            action = input('\n1. Посмотреть текущий текст чата.\n'
                           '2. Отправить сообщение.\n'
                           '3. - Сменить пользователя\n'
                           'end - Выйти из программы\n')
            print()
            if action == '1':
                try:
                    with open(path, 'r', encoding='utf-8') as read_file:
                        for i_line in read_file:
                            print(i_line, end='')
                except FileNotFoundError:
                    print('Чат ещё не создан!\n'
                          'Отправьте первое сообщение!\n'
                          '(введите 2)')
            elif action == '2':
                message = input(name + ': ')
                with open(path, 'a', encoding='utf-8') as write_file:
                    write_file.write(name + ': ' + message + '\n')
            elif action == '3':
                return True
            elif action == 'end':
                return False
            else:
                raise ValueError('Ошибка!\nВыберите один из предложенных вариантов.')
        except ValueError as error:
            print(error)

result = True
while result:
    name = input('Введите имя пользователя: ')
    result = writ_chat('chat.txt', name)