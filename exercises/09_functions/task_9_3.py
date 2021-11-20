# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv


def get_int_vlan_map(config_filename):
    port_access = {}
    port_trunk = {}
    with open(config_filename, "r") as conf:
        for line in conf:
            if "interface FastEthernet" in line:
                fa = line.split()[-1]

            if "access vlan" in line:
                pa = line.split()[-1]
                port_access[fa] = int(pa)

            if "trunk allowed vlan" in line:
                ta = line.split()[-1]
                # ta = [int(s) for s in ta.split(',')]
                ta = list(map(int, ta.split(',')))
                port_trunk[fa] = ta

    return port_access, port_trunk


# def get_int_vlan_map(config_filename):
#     access_dict = {}
#     trunk_dict = {}

#     with open(config_filename) as cfg:
#         for line in cfg:
#             line = line.rstrip()
#             if line.startswith("interface"):
#                 intf = line.split()[1]
#             elif "access vlan" in line:
#                 access_dict[intf] = int(line.split()[-1])
#             elif "trunk allowed" in line:
#                 trunk_dict[intf] = [int(v) for v in line.split()[-1].split(",")]
#         return access_dict, trunk_dict


# print(get_int_vlan_map(argv[1]))
