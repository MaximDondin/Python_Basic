students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def interests_n_surnames(data):
    list_of_interests = []
    surnames = ''
    for i_students in data:
        list_of_interests += (data[i_students]['interests'])
        surnames += data[i_students]['surname']
    return set(list_of_interests), len(surnames)

pairs = []
for i_students, i_value in students.items():
    pairs.append((i_students, i_value['age']))

interests, length_surname = interests_n_surnames(students)
print('Список пар "ID студента — возраст":', pairs)
print('Полный список интересов всех студентов:', interests)
print('Общая длина всех фамилий студентов:', length_surname)

