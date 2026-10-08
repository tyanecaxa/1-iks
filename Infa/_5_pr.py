# 1
# s = input()
# n = ''
# for i in s:
#     if i.isalpha():
#         if i != ' ':
#             n += i
# print(n)

# 2
# h = int(input())
# if h > 0:
#     k = 0
#     for i in range(1, h*2, 2):
#         k += 1
#         print(' '*(h-i+k)+'*'*i)
#         if h == 1:
#             break
#     print(' '*h+'*')
# else:
#     print('ERROR')

# 3
# def number_Armsrong(n):
#     s = str(n)
#     l = len(s)
#     n2 = 0
#     for i in s:
#         n2 += int(i)**l
#     if n2 == n:
#         return 1
#     else:
#         return 0

# n = int(input())
# k = 0
# for i in range(1, n+1):
#     if number_Armsrong(i):
#         k += 1
# print(k)

# 4
# text = input()
# word = input()
# ind = []
# for i in word:
#     ind.append(text.index(i))
# soind = ind[:]
# soind.sort()
# if ind == soind:
#     print('True')
# else:
#     print('False')

# 5
# import random
# n = random.randint(1,100)
# a = 1
# print(n)
# while a != 0:
#     d = int(input('Какое число загадано? '))
#     if d < n:
#         print('Больше')
#     elif d > n:
#         print('Меньше')
#     else:
#         a = 0
#         print('Угадал!')



# 6
# message = input("Введите сообщение: ").strip()

# if message == "":
#     print("Сообщение пустое. Пока.")
# else:
#     while True:
#         print("""
# Меню:
# 1.  Проверить на палиндром
# 2.  Подсчитать гласные
# 3.  Проверить, только ли цифры
# 4.  Проверить, только ли буквы
# 5.  Перевернуть строку
# 6.  В верхний регистр
# 7.  В нижний регистр
# 8.  Заменить пробелы на "_"
# 9.  Проверить, похоже ли на email
# 10. Извлечь домен
# 11. Выход
# """)

#         choice = input("Ваш выбор: ").strip()
#         mes_not_sim = ''.join([i for i in message if i.isalpha() or i.isdigit()])

#         match choice:
#             case "1":
#                 if mes_not_sim == mes_not_sim[::-1]:
#                     print('Сообщение является палиндромом!')
#                 else:
#                     print('Сообщение не является палиндромом!')
               
#             case "2":
#                 lower_msg = message.lower()
#                 count = (lower_msg.count("a") + lower_msg.count("e") +
#                          lower_msg.count("i") + lower_msg.count("o") +
#                          lower_msg.count("u"))
#                 print("Количество гласных:", count)
#             case "3":
#                 k = 0
#                 for i in message:
#                     if not(i.isdigit()):
#                         print('Есть буквы')
#                         break
#                     else:
#                         k += 1
#                 if k == len(message):
#                     print('Только цифры')
                
#             case '4':
#                 k = 0
#                 for i in message:
#                     if not(i.isalpha()):
#                         print('Есть цифры')
#                         break
#                     else:
#                         k += 1
#                 if k == len(message):
#                     print('Только буквы')

#             case '5':
#                 print(message[::-1])

#             case '6':
#                 print(message.upper())

#             case '7':
#                 print(message.lower())

#             case '8':
#                 print(message.replace(' ', '_'))

#             case '9':
#                 if '@' in message:
#                     m = message[message.index('@'):]
#                     if '.' in m:
#                         print('Email')
#                     else:
#                         print('Не email')
#                 else:
#                     print('Не email')

#             case '10':
#                 if '@' in message:
#                     m = message[message.index('@'):]
#                     if '.' in m:
#                         print('Домен: '+m[1:])
#                     else:
#                         print('Не email')
#                 else:
#                     print('Не email')

#             case "11":
#                 print("Выход. До связи).")
#                 break
#             case _:
#                 print("Неверный выбор. Попробуйте ещё раз.")



# 7
# email = input('Email: ')
# passw = input('Пароль: ')
# print()
# k = 0
# n = 0

# e = ['Email: ',email,' -> ']
# p = ['Пароль: ',passw,' -> ']

# if email.count('@') == 1:
#     s = email[email.index('@'):]
#     k += 1
# else:
#     e.append('x нет "@"')

# if '.' in s:
#     k += 1
# else:
#     e.append('x нет . после @')

# if email[0] != '@':
#     k += 1
# else:
#     e.append('x не должен начинаться с @')

# if email[-1] != '@':
#     k += 1
# else:
#     e.append('x не должен заканчиваться на @')

# if email[0] != '.':
#     k += 1
# else:
#     e.append('x не должен начинаться с .')

# if email[-1] != '.':
#     k += 1
# else:
#     e.append('x не должен заканчиваться на .')

# if 5 < len(email):
#     k += 1
# else:
#     e.append('x слишком короткий')

# if 30 > len(email):
#     k += 1
# else:
#     e.append('x слишком длинный')

# if k == 8:
#     e.append('OK')

# if e[3] == 'OK':
#     print(''.join(e))
# else:
#     print(''.join(e[:3]))
#     for i in e[3:]:
#         print(' '+i)

# if len(passw) > 7:
#     n += 1
# else:
#     p.append('x слишком короткий')

# if any (i.isdigit() for i in passw):
#     n += 1
# else:
#     p.append('x нет цифры')

# if any(i.isupper() for i in passw):
#     n += 1
# else:
#     p.append('x нет заглавной буквы')

# if any(i.islower() for i in passw):
#     n += 1
# else:
#     p.append('x нет строчной буквы')

# sp = passw.count('!')+passw.count('@')+passw.count('#')+passw.count('$')+passw.count('%')+passw.count('^')+passw.count('&')+passw.count('*')
# if sp > 0:
#     n += 1
# else:
#     p.append('x нет спецсимвола')

# if n == 5:
#     print(''.join(p))
# else:
#     print(''.join(p[:3]))
#     for i in p[3:]:
#         print(i)


# 8
# l1 = input().lower()
# l2 = input().lower()
# if l2.replace(' ', '') == '':
#     print('Не хайку. Должно быть 3 строки.')
# else:
#     l3 = input().lower()
#     if l3.replace(' ', '') == '':
#         print('Не хайку. Должно быть 3 строки.')
#     else:
#         k1 = 0
#         k2 = 0
#         k3 = 0

#         gl = 'аеёиоуыэюя'
#         for i in gl:
#             k1 += l1.count(i)
#             k2 += l2.count(i)
#             k3 += l3.count(i)

#         if k1 == k3 == 5 and k2 == 7:
#             print('Хайку!')
#         else:
#             print('Не хайку.')

# 9
# shiphr = input()
# if shiphr[-1] != '#':
#     print('Ошибка! Отсутствует символ #')
# else:
#     shiphr = shiphr[:-1]
#     ish = [i for i in shiphr if shiphr.index(i)%2==0]
#     print(ish)
#     ish.extend([i for i in shiphr[::-1] if shiphr.index(i)%2!=0])
#     print(ish)
# print(''.join(ish))
    
# доделать: 7,10