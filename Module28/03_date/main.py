class Date:
    def __init__(self, info: list) -> None:
        self.info = info
    def __str__(self) -> str:
        return f'День:{self.info[0]} \tМесяц:{self.info[1]} \tГод:{self.info[2]}'
    @classmethod
    def is_date_valid(cls, data: str) -> bool:
        result = data.split('-')
        __check_data = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     # Список дней по месяцам
        if int(result[2]) % 4 == 0 and int(result[2]) > 0:      # Проверка на високосный год
            __check_data[1] = 29
        if 1 <= int(result[1]) <= 12:
            if 1 <= int(result[0]) <= __check_data[int(result[1]) - 1]:
                if int(result[2]) > 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    @classmethod
    def from_string(cls, data: str):
        return cls(data.split('-'))


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))