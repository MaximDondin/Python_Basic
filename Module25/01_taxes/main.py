class Property:
    def __init__(self, worth, tarif):
        self.worth = worth
        self.tarif = tarif
        self.result = 0

    def __str__(self):
        self.result = self.worth * 1 / self.tarif
        return 'составил {} руб.'.format(self.result)
    def results(self):
        return self.result
class Apartment(Property):
    __tarif = 1000
    __worth = int(input('Сколько стоит дом? '))
    def __init__(self):
        super().__init__(self.__worth, self.__tarif)
    def __str__(self):
        return ''.join(('Налог на дом ', super().__str__()))

class Car(Property):
    __tarif = 200
    __worth = int(input('Сколько стоит машина? '))
    def __init__(self):
        super().__init__(self.__worth, self.__tarif)
    def __str__(self):
        return ''.join(('Налог на маину ', super().__str__()))

class CountryHouse(Property):
    __tarif = 500
    __worth = int(input('Сколько стоит дача? '))
    def __init__(self):
        super().__init__(self.__worth, self.__tarif)
    def __str__(self):
        return ''.join(('Налог на дачу ', super().__str__()))

money = int(input('Сколько у вас денег '))
apartment = Apartment()
car = Car()
countryhouse = CountryHouse()

print(apartment)
print(car)
print(countryhouse)

result = money - (apartment.results() + car.results() + countryhouse.results())
if result < 0:
    print('\nВам не хватает {} руб.'.format(result * (-1)))
else:
    print('\nВаш остаток {} руб.'.format(result))
