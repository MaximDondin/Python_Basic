import functools
from collections.abc import Callable
def decorator_with_args_for_any_decorator(decorator):
    def wrapped_decor(*args, **kwargs):
        @functools.wraps(decorator)
        def wrapped_func(func):
            result = decorator(func, *args, **kwargs)
            return result
        return wrapped_func
    return wrapped_decor
@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
print()
decorated_function("Юзер", 101)