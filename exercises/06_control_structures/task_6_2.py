# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# ip_addr = input("Введите IP-адрес:")
# # ip_addr = '0.0.0.0'
# list_ip_addr = ip_addr.split('.')
# i = 0
# j = 0
# for item in list_ip_addr:
#     if int(item) >= 1 and int(item) <= 223 and i == 0:
#         print('unicast')
#         break
#     elif int(item) >= 224 and int(item) <= 239 and i == 0:
#         print('multicast')
#         break

#     elif int(item) == 255:
#         j = j + 1
#         if j == 4:
#             print('local broadcast')

#     elif int(item) == 0:
#         j = j + 1
#         if j == 4:
#             print('unassigned')

#     else:
#         j = j + 1
#         if j == 4:
#             print('unused')

#     i = i + 1

ip_address = input("введите ip-адрес: ")
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
