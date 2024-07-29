import math


def get_sage_sqrt(num):
    try:
        if num < 0:
            raise ValueError('Ошибка! Число отрицательное.')
        return math.sqrt(num)
    except ValueError as exc:
        return str(exc)
    except Exception as exc:
        return 'Ошибка! {} не является числом'.format(exc)


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
