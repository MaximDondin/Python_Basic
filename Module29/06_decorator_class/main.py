import time
import functools
from typing import Callable

class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
    def __call__(self, *args, **kwargs) -> Callable:
        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы: {args}, {kwargs}')
        start_time = time.time()
        res = self.func(*args, **kwargs)
        end_time = time.time()
        print(f'Результат: {res}')
        print(f'Время выполнения: {end_time - start_time} секунд')
        return res
@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)