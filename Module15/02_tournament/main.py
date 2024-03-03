name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

def day(name_list, step):
    new_list = []
    for index in range(step, len(name_list), 2):
        new_list.append(name_list[index])
    return new_list

print('Первый день:', day(name_list, 0))
print('Второй день:', day(name_list, 1))
