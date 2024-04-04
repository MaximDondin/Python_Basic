def count_uppercase_lowercase(text):
    return sum(map(str.isupper, text)), sum(map(str.islower, text))

# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)

