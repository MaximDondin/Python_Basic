import os
import math
def sort_inf(path):
    file = open(path, 'r')
    frequency_letters = {}
    file_string = ''.join((litter.lower() for litter in file.read()
                   if litter.isalpha()))  # сразу убрал всё лишнее из строки, чтоб взять длину
    for litter in file_string:
        if frequency_letters.get(litter):
            frequency_letters[litter] += 1 / len(file_string)
        else:
            frequency_letters[litter] = 1 / len(file_string)
    frequency_letters = dict(
        sorted(frequency_letters.items(), key=lambda lit: lit[0]))  # сортировка по алфавиту
    frequency_letters = dict(
        sorted(frequency_letters.items(), key=lambda numb: numb[1], reverse=True))  # сортировка по числу
    file.close()
    return frequency_letters
def write_file(inf, path):
    file = open(path, 'w')
    for lit, num in inf.items():
        file.write(lit + ' ' + str(round(num, 3)) + '\n')
    file.close()

result = sort_inf(os.path.abspath('text.txt'))
write_file(result, os.path.abspath('analysis.txt'))