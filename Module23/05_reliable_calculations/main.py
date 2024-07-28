import math
def get_sage_sqrt(num):
    try:
        int(num)
        if num < 0:
            raise BaseException('Ошибка! Число отрицательное.')
        return math.sqrt(num)
    except Exception:
        return 'Ошибка! {} не является числом'.format(num)
    except BaseException as error:
        return error

# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")