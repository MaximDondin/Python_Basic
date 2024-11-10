import functools
from typing import Callable
def singleton(cls: Callable) -> Callable:
    cls.result = None
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not cls.result:
            cls.result = cls(*args, **kwargs)
            print(id(cls.result))
        return cls.result
    return wrapper
@singleton
class Example:
    pass

my_obj = Example
my_another_obj = Example

print(id(my_obj))
print(my_obj)
print(id(my_another_obj))
print(my_another_obj)


print(my_obj is my_another_obj)