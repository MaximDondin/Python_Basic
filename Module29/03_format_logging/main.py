import time
from datetime import datetime
from typing import Callable
import functools

def time_inf(cls: Callable, func: Callable, str_date: str) -> Callable:
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        new_date = str_date
        for symbol in new_date:
            if symbol.isalpha():
                new_date = new_date.replace(symbol, '%' + symbol)
        date_inf = datetime.now().strftime(new_date)
        print(f'- Запускается {cls.__name__}.{func.__name__}. Дата и время запуска: {date_inf}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'- Завершение {cls.__name__}.{func.__name__}, время работы = {end_time - start_time}')
        return result
    return wrapper

def log_methods(my_date: str) -> Callable:
    def decorated(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decor_method = time_inf(cls, cur_method, my_date)
                setattr(cls, i_method, decor_method)
        return cls
    return decorated

@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()