def calculation():
        shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

        part_name = input('\nНазвание детали: ')
        price = 0
        count = 0
        for i_name in shop:
                if i_name[0] == part_name:
                        count += 1
                        price += i_name[1]

        print('Кол-во деталей', count)
        print('Общая стоимость:', price)
        calculation()
calculation()