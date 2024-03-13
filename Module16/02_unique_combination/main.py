def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    list_sort = []

    for i_numb in range(len(list1)):
        for j_numb in range(i_numb + 1, len(list1)):
            if list1[i_numb] > list1[j_numb]:
                list1[i_numb], list1[j_numb] = list1[j_numb], list1[i_numb]

        if list1[i_numb - 1] != list1[i_numb] or i_numb == 0:
            list_sort.append(list1[i_numb])
    return list_sort

# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

merged = merge_sorted_lists(list1, list2)
if len(merged) == 0:
    print('Список пуст')
else:
    print('Отсортированный список без дубликатов', merged)