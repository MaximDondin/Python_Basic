import random

first_command = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_command = [round(random.uniform(5, 10), 2) for _ in range(20)]
result = [(first_command[player] if first_command[player] > second_command[player]
           else second_command[player]) for player in range(len(first_command))]

print('Первая команда:', first_command)
print('Вторая команда:', second_command)
print('Победители тура:', result)