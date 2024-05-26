def list_sorting(data, more = None, equal = None, less = None):
    if data:
        more, equal, less = helper(data)
        if equal == data:
            return data
        result = list_sorting(more) + list_sorting(equal) + list_sorting(less)
        return result
    return data
def helper(data):
    supporting_element = data[-1]
    more = []
    equal = []
    less = []
    for i_numb in data:
        if supporting_element > i_numb:
            more.append(i_numb)
        elif supporting_element == i_numb:
            equal.append(i_numb)
        else:
            less.append(i_numb)
    return more, equal, less

numb_list = [5, 9, 8, 4, 1, 2, 11, 8, 7, 6, 1, 0, -1]
print(list_sorting(numb_list))