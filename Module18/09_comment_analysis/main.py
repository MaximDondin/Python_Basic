def count_uppercase_lowercase(text):
    return (sum(letter.isupper() for letter in text),
            sum(letter.islower() for letter in text))

# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)

# TODO: зачем два "цикла", когда в один проход можно посчитать необходимое?
