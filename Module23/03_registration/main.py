def my_error(my_str):
    #print(my_str)
    try:
        if my_str:
            if len(my_str) < 3:
                raise IndexError
            for i_liter in my_str[0]:
                if not i_liter.isalpha():
                    raise NameError
            if '@' not in my_str[1] and '.' not in my_str[1]:
                raise SyntaxError
            if not int(my_str[2]) in range(10, 100):
                raise ValueError
            write_good(my_str)
    except IndexError:
        write_bad(my_str, 'НЕ присутствуют все три поля')
    except NameError:
        write_bad(my_str, 'Поле «Имя» содержит НЕ только буквы')
    except SyntaxError:
        write_bad(my_str, 'Поле «Имейл» НЕ содержит @ и . (точку)')
    except ValueError:
        write_bad(my_str, 'Поле «Возраст» НЕ является числом от 10 до 99')

def write_bad(my_str, error):
    # with open('registrations_bad.log', 'a', encoding='utf-8') as file_bad:
    #     file_bad.write(' '.join(my_str) + '\t\t' + error + '\n')
    file_bad.write(' '.join(my_str).ljust(37) + error + '\n')
def write_good(my_str):
    # with open('registrations_good.log', 'a', encoding='utf-8') as file_good:
    #     file_good.write(' '.join(my_str) + '\n')
    file_good.write(' '.join(my_str) + '\n')
def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        for i_line in file:
            my_error(i_line.rstrip().split())

file_bad = open('registrations_bad.log', 'w', encoding='utf-8')
file_good = open('registrations_good.log', 'w', encoding='utf-8')
r = read_file('registrations.txt')
file_bad.close()
file_good.close()
