def tpl_sort(data):
    data = list(data)
    transform(data)
    for i_numb in data:
        if type(i_numb) != int:
            return tuple(data)
    return tuple(sorted(data))
def transform(data):
    for i_index, i_numb in enumerate(data):
        if type(i_numb) == list or type(i_numb) == set:
            new_numb = list(i_numb)
            for j_index, j_numb in enumerate(new_numb):
                data.insert(i_index + j_index, j_numb)
            data.remove(i_numb)
    return data

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
print(tpl_sort((6, 3, -1, 8, 4, 10, -5, 'j')))
print(tpl_sort((6, 3, -1, 8, 4.2, 10, -5)))
print(tpl_sort((6, 3, -1, 8, [4], 10, -5)))
print(tpl_sort((6, 3, -1, 8, [4, 10], -5)))
print(tpl_sort((6, 3, -1, 8, {4, 7}, 10, -5)))
