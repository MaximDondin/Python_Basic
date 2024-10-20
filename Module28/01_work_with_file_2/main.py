class File:
    def __init__(self, path: str) -> None:
        self.path = path
    def __enter__(self): # Не знаю какой тип данных указать в аннотации
        file = open(self.path, 'a', encoding= 'utf-8')
        return file
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        file.close()
        #exc_list = ['FileExistsError', 'FileNotFoundError', 'IsADirectoryError', 'NotADirectoryError', 'PermissionError']
        if exc_type:
            return True


my_path = input('Укажите путь к файлу: ')
with File(my_path) as file:
    file.write(input('Файл открыт!\n') + '\n')