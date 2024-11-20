from collections import Counter
from typing import List

if __name__ == '__main__':
    def count_unique_characters(info: str) -> int:
        result: List[int] = list(filter(lambda litter: litter == 1, Counter(info.lower()).values()))
        return len(result)

    # Пример использования:
    message = "Today is a beautiful day! The sun is shining and the birds are singing."

    unique_count = count_unique_characters(message)
    print("Количество уникальных символов в строке:", unique_count)

else:
    print('Импортируется модуль -', __name__)