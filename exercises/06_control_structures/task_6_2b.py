# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input("введите ip-адрес: ")
list_ip_addr = ip_address.split('.')

check = True
if len(list_ip_addr) == 4:
    for item in list_ip_addr:
        if not (item.isdigit() and int(item) in range(0, 256)):
            check = False
            break
else:
    check = False

if check == False:
    print('Неправильный IP-адрес')
else:
    oct1 = int(ip_address.split(".")[0])

    if ip_address == "255.255.255.255":
        print("local broadcast")
    elif ip_address == "0.0.0.0":
        print("unassigned")
    elif 1 <= oct1 <= 223:
        print("unicast")
    elif 224 <= oct1 <= 239:
        print("multicast")
    else:
        print("unused")

sum = 0
num = []
for item in range(1, 20):
    if item % 2 != 0:
        num.append(4/item)

for item in range(0, len(num)):
    if item % 2 == 0:
        sum += num[item]
    if item % 2 != 0:
        sum -= num[item]

print(sum)
