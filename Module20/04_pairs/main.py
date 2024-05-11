import random
my_list = [random.randint(0, 9) for _ in range(10)]
print('Оригинальный список:', my_list)
new_list = [
    (my_list[i_numb], my_list[i_numb + 1])
    for i_numb in range(0, len(my_list), 2)
]
print('Новый список:', new_list)

new_list_2 = [
    tuple((my_list[j_numb + i_numb]) for j_numb in range(2))
    for i_numb in range(0, len(my_list), 2)
]
print('2-ой способ', new_list_2)

my_list_2 = my_list[1:]
new_list_3 = list(zip(my_list, my_list_2))
print('3-ий способ', new_list_3[::2])