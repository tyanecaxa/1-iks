# 1A
# import random
# bilet = []
# for i in range(6):
#     n = str(random.randint(1,49))
#     while n in bilet:
#         n = str(random.randint(1,49))
#     bilet.append(n)
# print(' '.join(bilet))

# 2B
# dni = list(map(int, input().split()))
# rost = []
# for i in range(len(dni)-1):
#     if dni[i] < dni[i+1]:
#         rost.append(str(dni[i+1]))
# print(" ".join(rost))

# 3C
# rost = input().split()
# rost.remove("/")
# x = rost[0]
# rost.remove(rost[0])

# poz = 1
# c = rost.count(x)

# for i in rost:
#     if i > x or i == x:
#         poz += 1
# print(poz)

# 4D
# import random
# hodi = []
# hodi.append(random.choice(['O','P']))
# p = 1
# i = 0
# while p != 3:
#     hodi.append(random.choice(['O','P']))
#     if hodi[i] == hodi[i+1]:
#         p += 1
#     else:
#         p = 1
#     i += 1
# print(f'{' '.join(hodi)} (попыток: {i+1})')
    
# 5E
# depths = list(map(int, input().split()))
# depthsb = depths[1:-1]
# m = []
# i = 0
# for s in depthsb:
#     if depths[i] < s and s > depths[i+2]:
#         m.append(s)
#     i += 1
# if m != []:
#     depths.remove(max(m))
# print(depths)

# 6F 
# n = input()
# n = [int(i) for i in n]
# print(n)
# s = n[-1]
# for i in range(0, len(n)-1):
#     s1 = n[i]
#     if i % 2 == 0:
#         s1 *= 2
#         if s1 > 9:
#             s1 -= 9
#     s += s1
#     print(s, s1)

# if s % 10 == 0:
#     print('Корректный номер')
# else:
#     print('Некорректный номер')

# 7G
# s = input().split()
# while '/' in s:
#     s.remove('/')
# c = int(s[0])
# s.remove(s[0])

# it = []
# for i in range(c):
#     l = len(s[i])
#     if l > 9:
#         it.append(f'{s[i][0]}{l-2}{s[i][-1]}')
#     else:
#         it.append(s[i])
# print(' / '.join(it))

# 8H
# k = input().split()
# while '/' in k:
#     k.remove('/')
# k = list(map(int, k))
# n = k[0]
# k.remove(k[0])

# c = 0
# for i in range(0, n*2,2):
#     if k[i] <= k[i+1]-2:
#         c += 1
# print(c)

# 9I
# l = input().split()
# l.remove("/")
# l = list(map(int, l))
# n, k, a = l[0], l[1], l[2:]

# if k > n:
#     s = k//n
#     k -= n*s

# zdv = list(map(str,l[-k:]+l[2:-k]))
# print(' '.join(zdv))

# 10L
# n, k = map(int, input().split())
# players = [str(i) for i in range(1, n+1)]
# lose = []
# x = 0

# while 1 < len(players):
#     x = (x + k - 1) % len(players)
#     lose.append(players.pop(x))

# print("Порядок выбывания: "+" ".join(lose)+'\nПобедитель: '+players[0])

# 11M
# trash = input().split(', ')
# trash[0] = trash[0][1:]
# trash[-1] = trash[-1][:-1]

# for i in range(len(trash)):
#     trash[i] = trash[i].strip('"').strip()
#     if trash[i] == '5' or trash[i] == 'отл':
#         trash[i] = 5
#     elif trash[i] == '4' or trash[i] == 'хор':
#         trash[i] = 4
#     elif trash[i] == '3' or trash[i] == 'уд':
#         trash[i] = 3
#     elif trash[i] == '2' or trash[i] == 'неуд':
#         trash[i] = 2
#     else:
#         trash[i] = ''

# trash = [i for i in trash if i != '']

# trash.sort(reverse=True)
# print(trash)
# x = 1
# while x < len(trash):
#     if trash.count(trash[x-1]) > 1:
#         del trash[x-1]
#     else:
#         x += 1

# print(trash)

# 12Q
# x = 0
# y = 0
# n, k = input().split(' / ')
# k = k.split(' ')
# for i in k:
#     match i:
#         case 'U':
#             y += 1
#         case 'D':
#             y -= 1
#         case 'L':
#             x -= 1
#         case 'R':
#             x += 1
# manh = abs(x) + abs(y)
# print(f'{x} {y} / {manh}')