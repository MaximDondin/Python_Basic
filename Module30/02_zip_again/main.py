from typing import List

if __name__ == '__main__':

    letters: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

    result: List[tuple] = list(map(lambda letter, numb: tuple([letter, numb]), letters, numbers))
    print('Мой аналог функции zip:\n', result)

else:
    print('Импортируется модуль -', __name__)