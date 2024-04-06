text = input('Введите строку: ')
count = 1
new_text = ''

for i_let in range(len(text)):
    if i_let == len(text) - 1:
        new_text += text[i_let] + str(count)
    elif text[i_let] == text[i_let + 1]:
        count += 1
    else:
        new_text += text[i_let] + str(count)
        count = 1
print(new_text)