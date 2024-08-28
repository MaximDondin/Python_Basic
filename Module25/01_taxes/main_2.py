class Property:
    __money = int(input('Сколько у вас денег? '))
    def __init__(self, worth):
        self.worth = worth
    def tax_calculation(self):
        pass
    def my_remains(self, *args):
        remains = self.__money
        for property in args:
            remains -= property.tax_calculation()
        if remains < 0:
            return ('\nВам не хватает {} руб.'.format(round(remains) * (-1)))
        else:
            return ('\nВаш остаток {} руб.'.format(round(remains, 2)))

class Apartment(Property):
    __tarif = 1000
    #__worth = int(input('Сколько стоит дом? '))
    def __init__(self):
        super().__init__(worth = int(input('Сколько стоит дом? ')))
    def tax_calculation(self):
        tax = self.worth * 1 / self.__tarif
        return tax
    def __str__(self):
        return ''.join(('Налог на дом ', str(self.tax_calculation()), ' руб.'))

class Car(Property):
    __tarif = 200
    #__worth = int(input('Сколько стоит машина? '))
    def __init__(self):
        super().__init__(worth = int(input('Сколько стоит машина? ')))
    def tax_calculation(self):
        tax = self.worth * 1 / self.__tarif
        return tax
    def __str__(self):
        return ''.join(('Налог на маину ', str(self.tax_calculation()), ' руб.'))

class CountryHouse(Property):
    __tarif = 500
    #__worth = int(input('Сколько стоит дача? '))
    def __init__(self):
        super().__init__(worth = int(input('Сколько стоит дача? ')))
    def tax_calculation(self):
        tax = self.worth * 1 / self.__tarif
        return tax
    def __str__(self):
        return ''.join(('Налог на дачу ', str(self.tax_calculation()), ' руб.'))


apartment = Apartment()
car = Car()
countryhouse = CountryHouse()

print(apartment)
print(car)
print(countryhouse)
print(apartment.my_remains(apartment, car, countryhouse))
