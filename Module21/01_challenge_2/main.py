def cycle(num):
    if num <= 1:
        print(num)
        return num
    cycle(num - 1)
    print(num)

cycle(int(input('Введите num: ')))