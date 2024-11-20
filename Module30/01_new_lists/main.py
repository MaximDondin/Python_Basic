from typing import List
from functools import reduce

if __name__ == '__main__':

    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    floats: List[float] = list(map(lambda numb: round(numb ** 3, 3), floats))
    names: List[str] = list(filter(lambda nam: len(nam) >= 5, names))
    numbers: int = reduce(lambda numb, count: int(numb) * count, numbers, 1)

    print('Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.\n -', floats)
    print('\nИз списка names берутся только те имена, в которых есть минимум пять букв.\n -', names)
    print('\nИз списка numbers берётся произведение всех чисел.\n -', numbers)

else:
    print('Импортируется модуль -', __name__)