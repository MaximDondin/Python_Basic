nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def straightened(data):
    new_list = []
    for i_numb in data:
        if isinstance(i_numb, list):
            new_list += straightened(i_numb)
        elif isinstance(i_numb, int):
            new_list.append(i_numb)
    return new_list


my_list = straightened(nice_list)
print(my_list)