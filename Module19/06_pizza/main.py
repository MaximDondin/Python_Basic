from num2words import num2words

size = int(input('Введите количество заказов: '))
total_order = {}

for i_numb in range(1, size + 1):
    order = input(f'{num2words(i_numb, lang = 'ru', to = 'ordinal')} заказ: ').split()
    if order[0] in total_order:
        if order[1] in total_order[order[0]]:
            total_order[order[0]][order[1]] += int(order[2])
        else:
            total_order[order[0]][order[1]] = int(order[2])
    else:
        total_order[order[0]] = {order[1]: int(order[2])}

print()
for i_key in sorted(total_order):
    print(f'{i_key}:')
    for j_key, j_value in sorted(total_order[i_key].items()):
        print(f'\t{j_key}: {j_value}')