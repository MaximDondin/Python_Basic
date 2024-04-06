ip_address = input('Введите IP: ').split('.')

if len(ip_address) < 4:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    for ip in ip_address:
        if not ip.isdigit():
            print(f'{ip} — это не целое число.')
            break
        if int(ip) > 255:
            print(f'{ip} превышает 255.')
            break
    else:
        print('IP-адрес корректен.')