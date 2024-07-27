import math
def get_sage_sqrt(num):
    try:
        try:
            int(num)
        except Exception:
            return 'Ошибка! {} не является числом.'.format(num)
        if num < 0:
            raise Exception('Ошибка! Число отрицательное.')
        return math.sqrt(num)
    except Exception as er:
        return er

# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")