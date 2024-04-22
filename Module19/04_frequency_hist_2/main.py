text = input("Введите текст: ")

def original_dictionary(text):
    frequency = {}
    for symbol in text:
        if symbol in frequency:
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1
    print('Оригинальный словарь частот:')
    for letter in sorted(frequency.keys()):
        print(letter, ':', frequency[letter])
    return frequency

def  inverted_dictionary(frequency):
    print('\nИнвертированный словарь частот:')
    new_frequency = {}
    for numb in range(1, max(frequency.values()) + 1):
        count = []
        for i_key, j_value in frequency.items():
            if j_value == numb:
                count.append(i_key)
        new_frequency[numb] = count
        print(numb, ':', new_frequency[numb])
    return new_frequency


inverted_dictionary(original_dictionary(text))
