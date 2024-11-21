from collections import Counter
from typing import List

if __name__ == '__main__':

    def can_be_poly(my_str: str) -> bool:
        result: List[int] = list(filter(lambda word: word % 2 != 0, Counter(my_str).values()))
        return False if len(result) > 1 else True

    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
    print(can_be_poly('abba'))
    print(can_be_poly('bbb'))
    print(can_be_poly('abca'))

else:
    print('Импортируется модуль -', __name__)