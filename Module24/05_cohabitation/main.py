import random
class Human:
    def __init__(self, name, house, satiety = 50):
        self.name = name
        self.satiety = satiety
        self.house = house

    def eat(self):
        self.satiety += 1
        self.house.refrigerator_with_food -= 1
        return 'eat'

    def work(self):
        self.satiety -= 1
        self.house.cabinet_with_money += 1
        return 'money'

    def play(self):
        self.satiety -= 1
        return 'play'

    def go_for_food(self):
        self.house.refrigerator_with_food += 1
        self.house.cabinet_with_money -= 1
        return 'food'

    def live_the_day(self, count = ''):
        num = random.randint(1, 6)
        if self.satiety < 0:
            print(self.name, 'DEAD')
            return False
        elif self.satiety < 20 and self.house.refrigerator_with_food > 0 + (count.find('food') + 1):  # использовал данну конструкцию дабы избежать ситуации, когда в один день заработали и сразу же купили
            print(f'{self.name}: Пошел кушать')  # данная конструкция позволяет иметь еду или деньги только в конце дня
            return self.eat()
        elif self.house.refrigerator_with_food < 10 and self.house.cabinet_with_money > 0 + (count.find('money') + 1):
            print(f'{self.name}: В магазин за едой')
            return self.go_for_food()
        elif self.house.cabinet_with_money < 50:
            print(f'{self.name}: На работу')
            return self.work()
        elif num == 1:
            print(f'{self.name}: Опять на работу')
            return self.work()
        elif num == 2:
            print(f'{self.name}: Опять кушать')
            return self.eat()
        else:
            print(f'{self.name}: Играть')
            return self.play()

class Home:
    def __init__(self, refrigerator_with_food = 50, cabinet_with_money = 0):
        self.refrigerator_with_food = refrigerator_with_food
        self.cabinet_with_money = cabinet_with_money

home = Home()
human1 = Human('Кирилл', home)
human2 = Human('Лена', home)

for day in range(365):
    print('День -', day)
    print(f'Сытость:\t{human1.name} - {human1.satiety} \t {human2.name} - {human2.satiety}')
    print('Еда в холодильнике:', human1.house.refrigerator_with_food)
    print('Деньги - тумбочке:', human1.house.cabinet_with_money)
    action1 = human1.live_the_day()
    action2 = human2.live_the_day(action1)
    print()
    if not action1 or not action2:
        break
else:
    print('Никто не умер')
