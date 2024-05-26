import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def site_copy(data): # создаёт копию, меняет название
    site_name = input('Введите название продукта для нового сайта: ')
    new_site = {f'Сайт для {site_name}:': copy.deepcopy(data)}
    rename(new_site, site_name)
    return new_site

def rename(data, name, key = 'телефон'): # меняет название товара
    for i_key, i_values in data.items():
        if key in i_values:
            data[i_key] = str(i_values).replace(key, name)
        if isinstance(i_values, dict):
            rename(i_values, name)
    return data

def site_header(data, numb): # Шапка сайтов
    for i_value in data:
        for j_key, j_value in i_value.items():
            print(j_key)
            print('site = {')
            print_of_site(j_value)
        print()

def print_of_site(data, deep = 2): # Вывод содержимого сайта
    for i_key, i_values in data.items():
        if isinstance(i_values, dict):
            print('\t' * deep, f'\'{i_key}\':', '{')
            print_of_site(i_values, deep + 2)
        else:
            print('\t' * deep, f'\'{i_key}\': \'{i_values}\'')
    print('\t' * (deep - 2), '}')

site_list = []
numb = int(input('Сколько сайтов: '))

if numb <= 0:
    print('Ошибка. Кол-во сайтов должно быть не менее 1')
else:
    for count in range(numb):
        site_list.append(site_copy(site))
        site_header(site_list, numb)
        #print(site_list)