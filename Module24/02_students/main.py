class Student:
    def __init__(self, fi, group_number, *grade):
        self.fi = fi
        self.group_number = group_number
        self.grade = sum(grade) / len(grade)
def sort_student():
    dict_student = {}
    for student in student_list:
        dict_student[student.grade] = [student.fi, student.group_number]
    dict_student = dict(sorted(dict_student.items()))
    for grade, info in dict_student.items():
        print(f'ФИ: {info[0]}, Номер группы: {info[1]}, Успеваемость: {grade}')

student_list = [Student('Ivanov Ivan', 327, 5, 3, 3, 4, 5),
                Student('Petrov Ivan', 327, 5, 5, 5, 5, 5),
                Student('Sidorov Misha', 217, 3, 5, 5, 3, 5),
                Student('Ivanov Sasha', 127, 5, 5, 3, 4, 5),
                Student('Mitin Ivan', 327, 5, 5, 2, 5, 5),
                Student('Kozlov Misha', 117, 3, 3, 3, 2, 5),
                Student('Molotov Ivan', 417, 5, 3, 2, 4, 5),
                Student('Baranov Ivan', 527, 5, 4, 5, 5, 5),
                Student('Molotov Misha', 217, 3, 5, 3, 2, 5),
                Student('Mitin Misha', 237, 3, 5, 3, 2, 5)]
sort_student()