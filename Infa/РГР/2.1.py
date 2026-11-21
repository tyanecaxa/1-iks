with open('movies.txt', 'r', encoding='utf-8') as f: #открытие файла
    l = f.readline().replace("\n","").split(";") #разбиение первой строки
    st = [] #записываем списки строк
    mx = 0
    mn = 100000

    for i in f:
        # разбиение строки по разделителю
        j = i.replace("\n", "").split(";")
        #преобразуем числа и дроби
        j[1],j[4],j[5],j[6],j[7] = \
        int(j[1]), int(j[4]), int(j[5]), int(j[6]), int(j[7]) 
        j[3] = float(j[3])
        st.append(j)
        #вычисляем максимальный и минимальный год
        if mx < j[1]:
            mx = j[1]
        if mn > j[1]:
            mn = j[1]
        
    print("Количество строк:", len(st))
    print(' '.join(l))
    for i in range(5):
        t = [str(j) for j in st[i]]
        print(' '.join(t))
    print('Минимальный год:', mn)
    print("Максимальный год:", mx)