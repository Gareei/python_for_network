# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Переделать скрипт: Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Подсказка: Для сортировки удобно сначала создать список списков такого типа,
а потом сортировать.

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

Сортировка должна быть по первому элементу (vlan), а если первый элемент одинаковый,
то по второму. Так работает по умолчанию функция sorted и метод sort, если сортировать
список списков выше.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
line_sort = []

with open('CAM_table.txt') as f:
    for line in f:
        line = line.split()
        if line and line[0].isdigit():
            line[0] = int(line[0])
            line_sort.append(line)
            # print("{:9}{:20}{}".format(line[0], line[1], line[3]))
line_sort.sort()
# print(line_sort)

for line in line_sort:
    # print("{:4}{:20}{}".format(line[0], line[1], line[3]))
    print(f"{line[0]:<9}{line[1]:20}{line[3]}")


# mac_table = []

# with open("CAM_table.txt", "r") as conf:
#     for line in conf:
#         words = line.split()
#         if words and words[0].isdigit():
#             vlan, mac, _, intf = words
#             mac_table.append([int(vlan), mac, intf])

# for vlan, mac, intf in sorted(mac_table):
#     print(f"{vlan:<9}{mac:20}{intf}")
