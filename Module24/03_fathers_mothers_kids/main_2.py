import random
class Parent:
    def __init__(self, name, age, *children):
        self.name = name
        self.age = age
        self.children = children
        for child in range(len(self.children)):
            if self.children[child].age > self.age - 16:
                raise ValueError(f'Ошибка!\nВозрать ребёнка {self.children[child].name} не может быть больше {self.age - 16}')

    def info(self):
        print(f'Имя: {self.name} \nВозраст: {self.age} \n'
              f'Дети: ' + ', '.join(self.children[numb].name for numb in range(len(self.children))))

    def child_calm(self):
        for child in range(len(self.children)):
            if self.children[child].state_calm:
                print(f'Ребёнок {self.children[child].name} - спокоен')
            else:
                print(f'Родитель успокоил ребёнка: {self.children[child].name}')
                self.children[child].state_calm = True

    def child_hunger(self):
        for child in range(len(self.children)):
            if self.children[child].state_hunger:
                print(f'Ребёнок {self.children[child].name} - сытый')
            else:
                print(f'Родитель покормил ребёнка: {self.children[child].name}')
                self.children[child].state_hunger = True

class Child:
    def __init__(self, name, age, state_calm=True,
                 state_hunger=True):
        self.name = name
        self.age = age
        self.state_calm = state_calm
        self.state_hunger = state_hunger

try:
    child_1 = Child('Лёша', 2, state_calm=random.choice([True, False]),
                    state_hunger=random.choice([True, False]))
    child_2 = Child('Миша', 5, state_calm=random.choice([True, False]),
                    state_hunger=random.choice([True, False]))
    parent_1 = Parent('Саша', 30, child_1, child_2)
    parent_1.info()
    print()
    parent_1.child_calm()
    parent_1.child_hunger()
except ValueError as error:
    print(error)
