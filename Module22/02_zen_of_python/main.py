def reverse(zen_path):
    file = open(zen_path, 'r')
    zen_revers = []
    # for i_line in file:
    #     zen_revers.append(i_line.strip('\n'))  # решил, что встроенная функция будет работать быстрее
    zen_revers = file.readlines()
    zen_revers.reverse()
    file.close()
    return zen_revers
def print_zen_reverse(zen):
    for i_line in zen:
        #print(i_line)
        print(i_line.strip('\n'))

result = reverse('zen.txt')
print_zen_reverse(result)