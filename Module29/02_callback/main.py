import functools
from typing import Callable
app = {}
def callback(path: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if path == '//':
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise Exception
            except Exception:
                return False
        app[path] = wrapped
        return wrapped
    return decorator

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
