class File:
    def __init__(self, path: str, mode: str) -> None:
        self.path = path
        self.mode = mode
        self.file = None
    def __enter__(self):
        try:
            self.file = open(self.path, self.mode, encoding='utf-8')
        except FileNotFoundError as error:
            self.mode = 'w'
            print(f'Такого файла не существует! \n{error}')
            print('Создаю новый!')
            self.file = open(self.path, self.mode, encoding='utf-8')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.mode == 'r':
            print(self.file.read())
        else:
            self.file.write(input() + '\n')
        self.file.close()
        #exc_list = ['FileExistsError', 'FileNotFoundError', 'IsADirectoryError', 'NotADirectoryError', 'PermissionError']
        if exc_type:
            return True


my_path = input('Укажите путь к файлу: ')
my_mode = input('В каком режиме открыть файл? \n"r" - чтение \n"w" - запись \n"a" - добавление \n')
with File(my_path, my_mode) as file:
    print('\nФайл открыт!')