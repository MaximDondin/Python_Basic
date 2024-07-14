import os
def serch(path):
    size_file_dir = [0, 0, 0]  # или лучше использовать 3 переменные (size, file, dir)?
    for i_object in os.listdir(path):
        new_path = os.path.join(path, i_object)
        if os.path.isfile(new_path):
            size_file_dir[0] += os.path.getsize(new_path) / 1024
            size_file_dir[1] += 1
        elif os.path.isdir(new_path):
            size_file_dir[2] += 1
            result = serch(new_path)
            size_file_dir = [size_file_dir[i_line] + result[i_line]
                             for i_line in range(len(size_file_dir))]
    return size_file_dir

size, file, dir = serch(input('Введите путь до желаемого каталога\n'))
print('Размер каталога (в Кб):', round(size, 2))
print('Количество подкаталогов:', dir)
print('Количество файлов:', file)