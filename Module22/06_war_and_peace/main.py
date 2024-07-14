import zipfile
import math
def unzip(path):
    myzip = zipfile.ZipFile(path, 'r')
    myzip.extractall()
def statistics_filtering(path):
    file = open(path, 'r', encoding='utf-8')
    frequency_letters = {}
    file_string = ''.join((litter for litter in file.read()
                           if litter.isalpha()))
    file.close()
    # file = open('intermediate_result.txt', 'w')       # промежуточный результат для проверки текста
    # file.write(file_string)
    # file.close()

    len_string = len(file_string)
    for litter in file_string:
        if frequency_letters.get(litter):
            frequency_letters[litter] += 1 / len_string
        else:
            frequency_letters[litter] = 1 / len_string
    frequency_letters = dict(
        sorted(frequency_letters.items(), key=lambda numb: numb[1], reverse=True))
    return frequency_letters

def write_file(inf, path):
    file = open(path, 'w')
    for lit, num in inf.items():
        file.write(lit + ' : ' + str(round(num, 6)) + '\n')
    file.close()

unzip('voina-i-mir.zip')
result = statistics_filtering('voyna-i-mir.txt')
write_file(result, 'statistics.txt')