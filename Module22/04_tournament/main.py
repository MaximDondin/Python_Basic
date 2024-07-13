def read_file(name_file):
    list_winners = {}
    file = open(name_file, 'r')
    scores = file.readline()
    for i_line in file:
        surname, name, rating = i_line.split()
        if int(rating) > int(scores):
            list_winners[name[0:1] + '. ' + surname] = rating
    list_winners = dict(sorted(list_winners.items(), key=lambda scores: scores[1], reverse=True))
    file.close()
    return list_winners
def write_file(list_winners):
    count = 1  # или использовать list(list_winners).index(fio) + 1, но экономит ли это память?
    file = open('second_tour.txt', 'w')
    file.write(str(len(list_winners)) + '\n')
    for fio, rating in list_winners.items():
        file.write(str(count) + ') ' + fio + ' ' + rating + '\n')
        count += 1
    file.close()

result = read_file('first_tour.txt')
write_file(result)
