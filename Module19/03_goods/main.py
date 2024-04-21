goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for name in goods:
    total_price = 0
    total_quantity = 0
    for j_len in range(len(store[goods[name]])):
        quantity = 0
        price = 0
        quantity, price = store[goods[i]][j].values()
        total_quantity += quantity
        total_price += quantity * price
    print(f'{i} - {total_quantity} штук, стоимость {total_price} рублей')