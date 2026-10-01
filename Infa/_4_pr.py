# 1
# a,b,c,d = int(input()),int(input()),int(input()),int(input())
# l = max(a,c)
# r = min(b,d)
# h = r-l

# if h > 0:
#     print(f"[{l}, {r}], длина {h}")
# elif h == 0:
#     print(f"точка {c}, длина 0")
# else:
#     print("Пересечений нет")

# 2
# st1,end1,st2,end2 = int(input()),int(input()),int(input()),int(input())

# l = max(st1,st2)
# r = min(end1,end2)
# h = r-l

# if h > 0:
#     print(f"YES")
# elif h == 0:
#     print(f"NO")
# else:
#     print("NO")

# 3
# minute, hour = int(input()), int(input())
# price = 0

# if 30 <= minute < 120:
#     price += 100
# elif 120 <= minute < 300:
#     price += 250
# elif minute >= 300:
#     price += 500

# if hour > 22 or hour < 6:
#     price += price*0.2
#     print(f"{price:.0f} ₽ (+20%)")
# else:
#     print(f"{price} ₽")

# 4
# code = int(input())

# match code:
#     case 100:
#         print('Ошибка конфигурации')
#     case 101:
#         print('Неизвестный параметр')
#     case 102:
#             print('Некорректное значение')
#     case 200:
#             print('Соединение установлено')
#     case 201:
#             print('Соединение разорвано')
#     case 300:
#             print('Ошибка авторизации')
#     case 301:
#             print('Доступ запрещён')
#     case 400:
#             print('Ошибка оборудования')
#     case 500:
#             print('Критическая ошибка')
#     case _:
#             print('Unknown error')

# 5
# dis, speed = int(input()), int(input())

# if dis <= 0.1 and speed <= 100:
#     print('WIFI')
# elif dis <= 10 and speed <= 150:
#     print('LTE')
# elif dis <= 2 and speed <= 1000:
#     print('5G')
# elif dis <= 1000 and speed <= 200:
#     print('SATELLITE')

# 6
# a,b,c,d = int(input()), int(input()), int(input()), int(input())
# if 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255:
#     if a == 127 and b==c==0 and d == 1:
#         print('LOOPBACK')
#     elif a==b==c==d==0:
#         print('UNSPECIFIED')
#     elif 224 <= a <= 239:
#         print('MULTICAST')
#     elif a==10 or (a==172 and 16 <= b <= 31) or (a==192 and b==168):
#         print('PRIVATE')
#     else:
#         print('PUBLIC')
# else:
#     print('INVALID')

# 7
# a,b,c,d = int(input()), int(input()), int(input()), int(input())
# if a==d==1:
#     print('CLOSED')
# elif (a==1 and b==0) or (c==d==1):
#     print('OPEN')
# else:
#     print('CLOSED')

# 8
# bnk,nnk,bkk,nkk = input(), int(input()), input(), int(input())
# b = ['a','b','c','d','e','f','g','h']
# k = 0

# for i in range(1,8):
#     if nkk == b.index(bkk)+i and nnk == b.index(bnk)+i:
#         k += 1
#         break
#     if nkk == b.index(bnk)+i and nnk == b.index(bkk)+i:
#         k += 1
#         break
# if bnk == bkk or (nnk > 8 or nkk > 8 or nnk < 1 or nkk < 1):
#     print('NO')
# elif k == 1:
#     print('YES')
# else:
#     print('NO')