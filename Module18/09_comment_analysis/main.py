def count_uppercase_lowercase(text):
    upper = 0
    lower = 0
    for letter in text:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return upper, lower

# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("\nКоличество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)