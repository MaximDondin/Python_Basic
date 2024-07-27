def open_file(path):
    line_count = 0
    sum_lit = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for i_line in file:
                line_count += 1
                try:
                    if len(i_line.rstrip()) < 3:
                        raise BaseException
                except BaseException:
                    with open('errors.log', 'w', encoding='utf-8') as file_error:
                        file_error.write('Ошибка: менее трёх символов в строке '
                                         + str(line_count))
                    print(f'Ошибка: менее трёх символов в строке {line_count}')
                sum_lit += len(i_line.rstrip())
        print(f'Общее количество символов: {sum_lit}')

    except FileNotFoundError:
        print('Файл не найден')
        with open('errors.log', 'w', encoding='utf-8') as file_error:
            file_error.write('Файл не найден')


open_file('people.txt')
