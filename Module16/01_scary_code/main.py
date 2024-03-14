first = [1, 5, 3]
side_a = [1, 5, 1, 5]
side_b = [1, 3, 1, 5, 3, 3]

first.extend(side_a)
print('Кол-во цифр 5 при первом объединении:', first.count(5))
for _ in range(first.count(5)):
    first.remove(5)
first.extend(side_b)
print('Кол-во цифр 3 при втором объединении:', first.count(3))
print('Итоговый список:', first)
