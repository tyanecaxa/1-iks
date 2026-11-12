# 1
# def func(x):
#     return x**2/10 + 1

# n = [10,100,1000,10000]
# a = -2
# b = 5
# p = 0
# for j in n:
#     s = 0
#     h = (b - a) / j
#     for i in range(0, j):
#         x_i = a + i*h
#         s += func(x_i)*h
#     print(f'n = {j}:'+' '*(len(n)-p)+f'{s:.2f}')
#     p += 1


# 2
# N = [10,100,1000]
# e = 0
# for j in N:
#     h = (b - a) / j
#     s = (h/2)*(func(a) + func(b))
#     s1 = 0
#     for i in range(1, j):
#         x_i = a + i*h
#         s1 += func(x_i)
#     s += s1*h
#     print(f'n = {j}:'+' '*(len(N)-e)+f'{s:.2f}')
#     e += 1

# 4
# from math import*
# n = int(input("Кол-во сокровищ: "))
# print('Координаты:', end=' ')
# k = []
# l = len('Координаты: ')
# for i in range(n):
#     k.append(list(map(int,input().split())))
# a = list(map(int,input("Координаты Александра: ").split()))

# r = 10000000000000
# c = 0
# for i in k:
#     s = dist(i,a)
#     if s < r:
#         r = s
#         c = i
# print(f"Ближайшее сокровище: {c[0]} {c[1]}")
# print(f'Расстояние: {r:.2f}')

# 5
# nums = [12, -5, 0, 7, 18, -3, 9, 24, 6, 15]
# ch = list(filter(lambda x: x % 2 == 0, nums))
# pol = list(filter(lambda x: x > 0, nums))
# kr = list(filter(lambda x: x % 3 == 0 and x > 5, nums))
# print(f'Чётные: {ch}')
# print(f'Положительные: {pol}')
# print(f'Кратные 3 и >5: {kr}')

# 6
# words = ["яблоко", "кот", "программирование", "дом", "молоко"]
# students = [("Аня", 20), ("Борис", 18), ("Вера", 22), ("Глеб", 19)]
# nums = [33, 12, 45, 21, 8, 99]

# l = sorted(words, key=lambda x: len(x))
# yo = sorted(students, key=lambda x: x[1])
# pc = sorted(nums, key=lambda x: x % 10)

# print("По длине: ",l)
# print("По возрасту: ",yo)
# print("По посл цифре: ", pc)

# 7
# students = [
#     ("Аня", 5), ("Борис", 3), ("Вера", 4),
#     ("Глеб", 5), ("Дина", 2), ("Егор", 4),
#     ("Жанна", 5), ("Зоя", 3)
# ]
# students = list(filter(lambda x: x[1] > 3, students))
# students = sorted(students, key=lambda x: (-x[1], x[0]))

# s = 0
# p = 0
# for n, c in students:
#     s += c
#     p += 1
#     print(f'{n} - {c}')
# print(f"Средний балл: {s/p}")

# 8
# def ryad(n, m, r, k): 
#     for i in r:
#         p = 1
#         for j in range(m-1):
#             if i[j] == i[j+1] == '0':
#                 p += 1
#             else:
#                 p = 1
#             if p >= k:
#                 return r.index(i)+1
#     return 0


# n, m = 5, 5 #list(map(int, input().split()))
# r = [ 
#     ['0', '1', '0', '0', '0'], 
#     ['1', '0', '0', '1', '0'], 
#     ['0', '0', '0', '0', '1'], 
#     ['1', '1', '1', '0', '0'], 
#     ['0', '0', '0', '0', '0']
# ]
# # for i in range(n):
# #     r.append(input().split())
# k = 3 #int(input())

# print(ryad(n,m,r,k))

# 9
# n, m = list(map(int, input().split()))
# mtx = []
# for i in range(n):
#     st = []
#     for j in range(m):
#         if j == 0 or i == 0:
#             st.append(1)
#         else:
#             st.append(0)
#     mtx.append(st)
# for i in range(1,n):
#     for j in range(1, m):
#         mtx[i][j] = mtx[i-1][j]+mtx[i][j-1]

# for i in range(n):
#     print(mtx[i])

# 10
# def tokenize(s):
#     l = []
#     r = '   \n.,;:!?()[]{}"«»…—–'
#     j = 0
#     for i in range(len(s)-1):
#         if s[i] in r and ' ' == s[i+1]:
#             l.append(s[j:i])
#             j = i
#     return l

# s = input()
# print(tokenize(s))

