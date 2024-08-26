import random
class KillError(Exception):
    def __str__(self):
        return 'Убийство'
    pass
class DrunkError(Exception):
    def __str__(self):
        return 'Пьянство'
    pass
class CarCrashError(Exception):
    def __str__(self):
        return 'Автокатастрофа'
    pass
class GluttonyError(Exception):
    def __str__(self):
        return 'Чревоугодие'
    pass
class DepressionError(Exception):
    def __str__(self):
        return 'Депрессия'
    pass

def one_day():
    karma_point = random.randint(1, 7)
    if random.randint(1, 10) == 5:
        raise random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
    return karma_point

karma = 0
const_karma = 500
with open('karma.log', 'w', encoding='utf-8') as file:
    while const_karma > karma:
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
            file.write(str(error) + '\n')
    print('Просветление достигнуто')