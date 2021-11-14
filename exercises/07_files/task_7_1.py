# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt') as f:
    for line in f:
        line = line.split()
        # line = (line[1:3])+(line[4:])
        pr, met, hop, lupd, intf = (line[1:3])+(line[4:])

        print(
            f"Prefix{pr:>29}\nAD/Metric{met.strip('[]'):>20}\nNext-Hop{hop[:-1]:>24}\nLast update{lupd[:-1]:>17}\nOutbound Interface{intf:>20}\n")

# with open("ospf.txt", "r") as f:
#     for line in f:
#         route = line.replace(",", " ").replace("[", "").replace("]", "")
#         route = route.split()

#         print(output.format(
#                 "Prefix", route[1],
#                 "AD/Metric", route[2],
#                 "Next-Hop", route[4],
#                 "Last update", route[5],
#                 "Outbound Interface", route[6],
#         ))
