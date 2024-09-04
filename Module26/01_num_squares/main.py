class MyIterator:
    def __init__(self, numb: int) -> None:
        self.__numb = numb
        self.__count = 0
    def __iter__(self) -> iter:
        return self
    def __next__(self) -> int:
        if self.__count < self.__numb:
            self.__count += 1
            return self.__count ** 2
        else:
            raise StopIteration

def generator_function(numb: int) -> int:
    for number in range(1, numb + 1):
        yield number ** 2

print('Класс-итератор')
my_iter = MyIterator(10)
for numb in my_iter:
    print(numb, end = ' ')

print('\n\nФункция-генератор')
for numb in generator_function(10):
    print(numb, end = ' ')

print('\n\nГенераторное выражение')
expression_generator = (numb ** 2 for numb in range(1, 11))
for numb in expression_generator:
    print(numb, end = ' ')
print()
