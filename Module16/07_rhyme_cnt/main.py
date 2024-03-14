people = list(range(1, (int(input('Кол-во человек: '))) + 1))
stop_numb = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {stop_numb}-й человек')
start_numb = 0
count = 0
length_const = len(people)

for index in range(len(people)):
    if index < length_const - 1:
        print('\nТекущий круг людей:', people)
        print('Начало счёта с номера', people[start_numb])
        count = stop_numb - len(people) * (stop_numb // len(people))
        if count == 0:
            count = stop_numb // (stop_numb // len(people))
        start_numb += count - 1
        if start_numb == len(people):
            start_numb = 0
        print('Выбывает человек под номером', people[start_numb])
        people.remove(people[start_numb])
        if start_numb == len(people):
            start_numb = 0
    else:
        print('\nОстался человек под номером', people[start_numb])