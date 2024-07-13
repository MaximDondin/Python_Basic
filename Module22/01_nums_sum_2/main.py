def search_summ(numbers_path):
    file_numbers = open(numbers_path, 'r')
    result = 0
    for i_line in file_numbers:
        result += sum(map(int, i_line.split()))
    file_numbers.close()
    return result

def write_summ(answer_path, summ):
    file_answer = open(answer_path, 'w')
    file_answer.write(str(summ))
    file_answer.close()

summ = search_summ('numbers.txt')
write_summ('answer.txt', summ)