import os
def gen_files_path(search_dir: str, path: str) -> str:
    for root, dirs, files in os.walk(path):
        if search_dir == root.split('\\')[-1]:
            for file in files:
                yield os.path.join(root, file)
            break
    else:
        print(f'Каталога "{search_dir}" нет в директории: {path}')

path = input('Введите директорию искомого каталога (если неизвестно, оставьте поле пустым): ')
path = os.path.abspath(os.path.sep) if not path else path
while True:
    directory = input('Введите название каталога: ')
    if not directory:
        print('\nВы не указали искомый каталог')
    else:
        break
file_path = gen_files_path(directory, path)
for i_path in file_path:
    print(i_path)