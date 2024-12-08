import re
import requests

if __name__ == '__main__':
    # В данном случае запрос request.get заменен на загрзку сайта из файла html
    with open('examples.html', 'r') as f:
        text = f.read()
    # По итогу вы так же получаете код сайта в виде одной строки

    pattern = r'<h3>(.*?)</h3>'
    result = re.findall(pattern, text)
    print(result)

    my_requests = requests.get('https://4pda.to/forum/index.php?showuser=11085064')
    res = re.findall(pattern, my_requests.text)
    print(res)

    my_requests2 = requests.get('https://habr.com/ru/articles/349860/')
    res2 = re.findall(pattern, my_requests2.text)
    print(res2)

else:
    print('Импортируется модуль -', __name__)