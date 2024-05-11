phone_book = {
#    ('Иван', 'Сидоров'): 888,
#    ('Миша', 'Сидоров'): 555
}
def actions():
    print('\nВведите номер действия:')
    print('\t1. Добавить контакт \n\t2. Найти человека')
    action = int(input())
    if action == 1:
        add_contact()
    elif action == 2:
        search()
    else:
        print('Такого действия нет\n')
        actions()

def add_contact():
    surname_name = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()
    if phone_book.get(tuple(surname_name), False):
        print('Такой человек уже есть в контактах.')
    else:
        numb = input('Введите номер телефона: ')
        phone_book[(surname_name[0], surname_name[1])] = numb
    print('Текущий словарь контактов:', phone_book)
    actions()

def search():
    flag = True
    surname = input('Введите фамилию для поиска: ').title()
    for surname_name, numb in phone_book.items():
        if surname in surname_name:
            print(f'{surname_name[0]} {surname_name[1]} : {numb}')
            flag = False
    if flag:
        print('Такого человека нет в контактах')
    actions()

actions()