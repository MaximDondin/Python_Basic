count = 0
skates_list = []
people_list = []

def check():
    while True:
        skates = (int(input('\nКол-во коньков: ')))
        if skates <= 0:
            print('Ошибка ввода')
        else:
            skates_size(skates)
            break
    while True:
        people = (int(input('\nКол-во людей: ')))
        if people <= 0:
            print('Ошибка ввода')
        else:
            people_size(people)
            break
def skates_size (skates):
    for i_skates in range(skates):
        print(f'Размер {i_skates + 1}-й пары: ', end = '')
        size = int(input())
        skates_list.append(size)
    return skates_list

def people_size(people):
    for i_people in range(people):
        print(f'Размер ноги {i_people + 1}-го человека: ', end = '')
        size = int(input())
        people_list.append(size)
    return people_list


check()
for i_couple in people_list:
    for j_couple in skates_list:
        if i_couple == j_couple:
            count += 1
            skates_list[skates_list.index(j_couple)] = -1
            break
print('\nНаибольшее кол-во людей, которые могут взять ролики:', count)