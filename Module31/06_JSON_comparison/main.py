import json
from typing import Any, List

if __name__ == '__main__':
    # diff_list = ["services", "staff", "datetime"]
    diff_list = ["cost", "datetime"]
    diff_data = {}

    def search_differences(data_1: Any, data_2: Any, diff: List) -> None:
        """Функция для поиска изменений в файлах json_old.json и json_new.json по заданным ключам из списка diff_list"""
        if isinstance(data_2, dict) and isinstance(data_1, dict):
            for key, value in data_2.items():
                if isinstance(value, dict):
                   search_differences(data_1[key], data_2[key], diff)
                if (data_1[key] != data_2[key]) and (key in diff):
                    diff_data[key] = value
                elif isinstance(value, list):
                    while len(data_1[key]) > 0 and len(data_2[key]) > 0:
                        search_differences(data_1[key][0], data_2[key][0], diff)
                        data_1[key].pop(0)
                        data_2[key].pop(0)


    with open('json_old.json', 'r', encoding='utf-8') as file:
        data_old = json.load(file)

    with open('json_new.json', 'r', encoding='utf-8') as file:
        data_new = json.load(file)

    search_differences(data_old, data_new, diff_list)
    print(json.dumps(diff_data, indent=4, ensure_ascii=False))

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(diff_data, file, indent=4, ensure_ascii=False)

else:
    print('Импортируется модуль -', __name__)