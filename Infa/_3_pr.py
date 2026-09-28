#№1
# fio = input("Введи первые буквы ФИО: ")
# for i in fio:
#     print(i, ord(i))

#№2
# print('Информатика'.encode('utf-8'))
# print('Информатика'.encode('cp1251'))

#№3
# s = input("Введите строку: ")
# print("Символов в строке: ", len(s))
# print("Байтов в UTF-8: ", len(s.encode('utf-8')))
# print("Байтов в CP1251: ", len(s.encode('cp1251')))

#№4
# a = b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8'
# b = b'\xd1\x88\xd0\xbf\xd0\xb0\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbb\xd0\xba\xd0\xb0'
# c = b'\xca\xee\xe4\xe8\xf0\xee\xe2\xea\xe8'
# print(a.decode('utf-8'), b.decode('utf-8'), c.decode('cp1251'))

#№5
# s = input('Введи символы: ')
# for i in s:
#     print(i, ord(i), len(i.encode('utf-8')))

#№6
# t = "Сообщение".encode('utf-8').decode('cp1251')
# print(t)
# print(t.encode('cp1251').decode('utf-8'))

#№7
# vob = int(input('Размер(ГБ): '))
# vz = int(input('Скорость интернета(Мбит/с: '))
# tmin = int(input('Время установки(мин): '))
#
# vob *= 1024*8
#
# tsk = vob // vz
# tsk_min = tsk // 60
# tsk_sec = tsk % 60
#
# ob = tsk + tmin*60
# ob_min = ob // 60
# ob_sec = ob % 60
#
# print(f"Время скачивания: {tsk_min:02d}:{tsk_sec:02d}")
# print(f"Общее время: {ob_min:02d}:{ob_sec:02d}")

#№8
# kolvo = int(input("Кол-во товаров: "))
# v_kont = int(input("Вместимость одного контейнера: "))
#
# pol = kolvo//v_kont
# ost = kolvo - pol*v_kont
# ef = float(1 - (ost/kolvo))*100
#
# print("Полных контейнеров: ", pol)
# print("Оставшийся товар: ", ost)
# print(f"Эффективность упаковки: {ef:.2f}%")

#№9
# n = input("Номерной знак: ")
# f = ''
# for i in n:cd
#     if i.isdigit():
#         f += '0'
#     elif i.isalpha():
#         f += '1'
#     else:
#         f += '-'
# if f == '111000':
#     print("Старый номер")
# elif f == '1110000':
#     print('Новый номер')
# else:
#     print('Не номер машины')