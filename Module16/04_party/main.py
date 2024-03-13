
def party():
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'пора спать' or answer == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
    else:
        name = input('Имя гостя: ')
        if answer == 'пришел' or answer == 'пришёл':
            if len(guests) >= 6:
                print(f'Прости, {name}, но мест нет.')
                party()
            else:
                print(f'Привет, {name}!')
                guests.append(name)
                party()
        elif answer == 'ушел' or answer == 'ушёл':
            if guests.count(name) == 0:
                print('Такого гостя нет')
                party()
            else:
                print(f'Пока, {name}!')
                guests.remove(name)
                party()

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
party()