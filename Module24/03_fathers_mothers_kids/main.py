import random
class Parent:
    def __init__(self, name, age, *children):
        self.name = name
        self.age = age
        self.children = children
    def info(self):
        print(f'Имя: {self.name} \nВозраст: {self.age} \nДети: ' + ', '.join(self.children))
    def child_calm(self, count):
        if isinstance(count, Child):
            if count.name in self.children and count.parent:
                if count.state_calm:
                    print(f'Ребёнок: {count.name} спокоен')
                else:
                    print(f'Родитель: {self.name} успокоил ребёнка: {count.name}')
                    count.state_calm = True
            else:
                print(f'{count.name} не является ребёнком родителя: {self.name}')
    def child_hunger(self, count):
        if isinstance(count, Child):
            if count.name in self.children and count.parent:
                if count.state_hunger:
                    print(f'Ребёнок: {count.name} сытый')
                else:
                    print(f'Родитель: {self.name} покормил ребёнка: {count.name}')
                    count.state_hunger = True
            else:
                print(f'{count.name} не является ребёнком родителя: {self.name}')

class Child:
    def __init__(self, parent, name, age, state_calm = True,
                 state_hunger = True):
        try:
            self.parent = parent
            self.name = name
            if parent:
                if self.name in parent.children:
                    if age <= parent.age - 16 and parent.age - 16 > 0:
                        self.age = age
                    else:
                        raise ValueError(f'Неверно указан возраст ребенка {name}')
                else:
                    raise ValueError(f'У родителя: {parent.name} нет ребёнка {name}')
            else:
                self.age = age
            self.state_calm = state_calm
            self.state_hunger = state_hunger
        except ValueError as error:
            print(error)


# Моя задумка в том, что ребёнок привязывается к определенному родителю
# И чужой родитель не может покормить или успокоить ребёнка
try:
    parent_1 = Parent('Саша', 25, 'Лёша', 'Катя')
    parent_2 = Parent('Андрей', 25, 'Миша', 'Лена')
    child_1 = Child(parent_1, 'Лёша', 2, state_calm = random.choice([True, False]),
                 state_hunger = random.choice([True, False]))
    child_2 = Child(parent_2, 'Миша', 1, state_calm = random.choice([True, False]),
                 state_hunger = random.choice([True, False]))
    #print('Состояние спокойствия ребёнка:', child_1.name, '-', child_1.state_calm)
    parent_1.child_calm(child_1)
    #print('Состояние спокойствия ребёнка:', child_1.name, '-', child_1.state_calm)
    print()

    #print('Состояние голода ребёнка:', child_1.name, '-', child_1.state_hunger)
    parent_1.child_hunger(child_1)
    #print('Состояние голода ребёнка:', child_1.name, '-', child_1.state_hunger)
    print()

    #print('Состояние голода ребёнка:', child_2.name, '-', child_2.state_hunger)
    parent_1.child_hunger(child_2)
    #print('Состояние голода ребёнка:', child_2.name, '-', child_2.state_hunger)
except BaseException:
    print('Проверьте данные')