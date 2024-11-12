import functools
from typing import Callable
def check_permission(user: str) -> Callable:
    def wrap_fun(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if user in user_permissions:
                    result = func(*args, **kwargs)
                else:
                    raise PermissionError('PermissionError')
                return result
            except PermissionError as error:
                print(f'{error}: У пользователя недостаточно прав, чтобы выполнить функцию {wrapped.__name__}')
        return wrapped
    return wrap_fun

user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()