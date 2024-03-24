import string

def cipher(text):
    step = int(input('Введите сдвиг: '))
    count = ''
    alphabet = [['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
                'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'],
                [' ', '.', '!', '?', ',']]
    for i in range(len(text)):
        for j in range(len(alphabet[0])):
            if text[i] == alphabet[0][j - step % len(alphabet[0])]:
                count += alphabet[0][j]
            elif text[i] == string.capwords(alphabet[0][j - step % len(alphabet[0])]):
                count += string.capwords(alphabet[0][j])
        for k in range(len(alphabet[1])):
            if text[i] == alphabet[1][k]:
                count += alphabet[1][k]
    return count

message = input('Введите сообщение: ')
print('Зашифрованное сообщение:', cipher(message))