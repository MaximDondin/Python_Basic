ban = '@', '№', '$', '%', '^', '&', '*', '(', ')', '\\'
name = input('Название файла: ')

if name.startswith(ban):
    print('Ошибка: название начинается на один из специальных символов.')
    # TOOD: зачем дважды метод вызывать, когда в него можно сразу передать несколько аргументов?
    # https://pythonz.net/references/named/str.startswith/
elif not name.endswith('.txt') and not name.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')
