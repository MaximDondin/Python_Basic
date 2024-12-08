import requests
import json
from typing import Any

if __name__ == '__main__':
    pilots_data = {'name': 0, 'height': 0, 'mass': 0, 'homeworld': 0, 'homeworld_url': 0}   # Словари для упорядоченного сбора информации
    ship_data = {'ship_name': 0, 'starship_class': 0, 'max_atmosphering_speed': 0, 'pilots': 0}

    def planet_name(info: Any) -> Any:
        """Функция для нахождения названия планеты
        принимает на вход любой тип данных
        рекурсивно ищёт по ключу нужное значение(любого типа) и возвращает его"""
        if isinstance(info, dict):
            for key, value in info.items():
                if key == 'name':
                    return value
                else:
                   name = planet_name(value)
                   if name:
                       return name

    def search_pilots(info: Any) -> None:
        """Функция для сбора информации о пилотах
        принимает на вход любой тип данных
        рекурсивно ищёт по ключу нужное значение и добавляет в словарь pilots_data"""
        if isinstance(info, dict):
            for key, value in info.items():
                if key in pilots_data:
                    if key == 'homeworld':
                        pilots_data[key] = planet_name(requests.get(value).json())
                        key = 'homeworld_url'
                    pilots_data[key] = value
                else:
                    search_pilots(value)

    def search_ship(info: Any) -> None:
        """Функция для сбора информации по кораблю X-wing
        принимает на вход любой тип данных
        рекурсивно ищёт по ключу нужное значение и добавляет в словарь ship_data"""
        if isinstance(info, dict):
            for key, value in info.items():
                if key == 'name':
                    key = 'ship_name'
                if key in ship_data:
                    ship_data[key] = value
                else:
                    search_ship(value)

    my_request = requests.get('https://www.swapi.tech/api/starships/12/')
    if my_request.status_code == 200:
        data = json.loads(my_request.text)
        search_ship(data)
        while True:
            if isinstance(ship_data['pilots'][0], dict):
                break
            search_pilots(requests.get(ship_data['pilots'][0]).json())
            ship_data['pilots'].pop(0)
            ship_data['pilots'].append(pilots_data.copy())

        with open('my_test.json', 'w') as file:
            json.dump(ship_data, file, indent=4)

        print(json.dumps(ship_data, indent=4))

else:
    print('Импортируется модуль -', __name__)