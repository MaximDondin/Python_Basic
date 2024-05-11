def tpl_sort(data):
    for i_numb in data:
        if type(i_numb) != int:
            return tuple(data)
    return tuple(sorted(data))

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
print(tpl_sort((6, 3, -1, 8, 4, 10, -5, 'j')))
print(tpl_sort((6, 3, -1, 8, 4.2, 10, -5)))
print(tpl_sort((6, 3, -1, 8, [4], 10, -5)))
print(tpl_sort((6, 3, -1, 8, [4, 10], -5)))
print(tpl_sort((6, 3, -1, 8, {4, 7}, 10, -5)))
