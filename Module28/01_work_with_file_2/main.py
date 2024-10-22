class File:
    def __init__(self, path: str) -> None:
        self.path = path
        self.mode = None
        self.file = None
    def __enter__(self):
        try:
            self.mode = input('В каком режиме открыть файл? \n"r" - чтение \n"w" - запись \n"a" - добавление \n')
            self.file = open(self.path, self.mode, encoding='utf-8')
        except:
            self.mode = 'w'
            print('Такого файла не существует!')
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
with File(my_path) as file:
    print('\nФайл открыт!')