def my_sum(*args):
    summa = 0
    for i_numb in args:
        if isinstance(i_numb, int):
            summa += i_numb
        elif isinstance(i_numb, (list, set)):
            summa += sum_list(i_numb)
    return summa

def sum_list(data):
    summa = 0
    for j_numb in data:
        if isinstance(j_numb, (list, set)):
            summa += my_sum(j_numb)
        elif isinstance(j_numb, int):
            summa += j_numb
    return summa


#print(my_sum([[1, 2, [{3}]], [1], 3]))
#print(my_sum(1, 2, {3}, 4, 5))
#print(my_sum([[{1: 55}, {3: [5, 6]}, 2, [3]], [1], 3]))
