import os
def counting_rows(path: str) -> str:
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as py_file:
                    result = py_file.readlines()
                    for line in result:
                        if line.startswith('#') or line.startswith('\n'):
                            continue
                        else:
                            count += 1
                    yield f'Файл: {os.path.join(root, file)} \nСодержит {count} строк\n'
                    count = 0

size = counting_rows('C:\\Users\\Max\\PycharmProjects\\Python_Basic\\Module26')
for info in size:
    print(info)