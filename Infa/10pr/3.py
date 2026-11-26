with open("files/olimp.txt",'r',encoding='utf-8') as f:
    name = ''
    b = 0
    for i in f:
        i = i.rsplit(maxsplit=1)
        c = int(i[-1])
        if c > b:
            name = i[0]
            b = c
print(f'{name} {b}')