site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def search(data, key, deep):
	result = None
	if deep <= 0:
		return result

	if key in data:
		return data[key]

	for i_values in data.values():
		if isinstance(i_values, dict):
			result = search(i_values, key, deep - 1)
			if result:
				return result
	return result


my_key = input('Введите искомый ключ: ')
question_of_deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()
max_deep = None
if question_of_deep == 'y':
    max_deep = int(input('Введите максимальную глубину: '))

print('Значение ключа:', (search(site, my_key, max_deep)))