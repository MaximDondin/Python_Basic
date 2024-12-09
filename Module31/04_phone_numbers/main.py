import re

if __name__ == '__main__':
    number_list = ['9999999999', '999999-999', '99999x9999', '9234567890', '0123456789']
    my_num2words = ['первый', 'второй', 'третий', 'четвертый', 'пятый']
    pattern = r'\b[89]\d{9}\b'

    count = 0
    for number in number_list:
        result = re.findall(pattern, number)
        if result:
            print(f'{my_num2words[count]} номер ({number_list[count]}): все в порядке')
            # print(f'{num2words(count + 1, to='ordinal', lang='ru')} номер ({number_list[count]}): все в порядке')
        else:
            print(f'{my_num2words[count]} номер ({number_list[count]}): не подходит')
            # print(f'{num2words(count + 1, to='ordinal', lang='ru')} номер ({number_list[count]}): не подходит')
        count += 1

else:
    print('Импортируется модуль -', __name__)