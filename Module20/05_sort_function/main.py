def tpl_sort(data):
    for i_numb in data:
        if not i_numb.is_integer():
            return data
    return tuple(sorted(data))

# tpl = (6, 3, -1, 8, 4.5, 10, -5)
# print(tpl_sort(tpl))