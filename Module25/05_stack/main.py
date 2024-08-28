class Stack:
    def __init__(self):
        self.stack_list = []
    def add_stack(self, data):
        self.stack_list.append(data)
    def pop_stack(self):
        self.stack_list.pop()
    def __str__(self):
        print('\nЧто хранится в стейке:')
        for data in self.stack_list:
            print(data)
        return ''

class TaskManager:
    def __init__(self):
        self.stac = Stack()
        self.stac_dict = {}
    def new_task(self, task, priority):
        try:
            for data in self.stac.stack_list:
                if task in data:
                    raise ValueError
            self.stac.add_stack([task, priority])
        except ValueError:
            print(f'Задача "{task}" уже существует.\nСначала завершите её')
    def check_list(self, task):         # Слишком много циклов! Как можно это сократить? Сделал этот метод для проверки стейка перед удалением
        if len(self.stac.stack_list) == 0:
            print('Стейк пустой\n')
        else:
            for data in self.stac.stack_list:
                if task in data:
                    self.del_task(task)
                    break
            else:
                print('\nТакой задачи нет!')

    def del_task(self, task):
        self.stac.pop_stack()
        for data in self.stac.stack_list:
            if task in data:

                self.del_task(task)
                break
    def __str__(self):
        for data in self.stac.stack_list:
            self.stac_dict[data[0]] = data[1]
        count = 0
        print('Результат:', end='')
        self.stac_dict = sorted(self.stac_dict.items(), key=lambda x: x[1])
        for data in self.stac_dict:
            if count == data[1]:
                print(f'; {data[0]}', end='')
            else:
                count = data[1]
                print(f'\n{data[1]} - {data[0]}', end='')
        self.stac_dict = {}
        return '\n'

manager = TaskManager()
manager.check_list("сдать ДЗ")        # удаление из пустого стейка
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
manager.new_task("сдать ТК", 7)
manager.new_task("сдать ТК", 8)         # Дубликат, который не внесётся в стейк
manager.new_task("приготовить еду", 6)
manager.check_list("сдать")         # удаление несуществующей задачи

print(manager.stac.__str__())
print(manager)

print('удаляем ("сдать ДЗ")\n')
manager.check_list("сдать ДЗ")

print(manager)
