import re

if __name__ == '__main__':
    text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

    cars_pattern = r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
    taxi_pattern = r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'

    cars = re.findall(cars_pattern, text)
    taxi = re.findall(taxi_pattern, text)

    print('Список номеров частных автомобилей:', cars)
    print('Список номеров такси:', taxi)

else:
    print('Импортируется модуль -', __name__)