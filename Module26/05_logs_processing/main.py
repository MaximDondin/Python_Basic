import os

def error_log_generator(path: str) -> str:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as input:
            for line in input.readlines():
                if line.startswith('ERROR'):
                    yield line
    else:
        raise FileNotFoundError('Такого пути не существует!')

input_file_path = os.path.abspath(os.path.join('data', 'work_logs.txt'))
output_file_path = os.path.abspath(os.path.join('data', 'output.txt'))

with open(output_file_path, 'w', encoding='utf-8') as output:
    try:
        for error_line in error_log_generator(input_file_path):
            output.write(error_line)
        print("Файл успешно обработан.")
    except FileNotFoundError as error:
        output.write(str(error))
        print(error)