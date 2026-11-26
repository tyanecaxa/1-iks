with open("files/secret.txt",'r',encoding='utf-8') as f1:
    with open('files/secret_annonymized.txt','w',encoding='utf-8') as f2:
        for i in f1:
            i = i.rsplit(maxsplit=4)
            i[-1] += '\n'

            i[2] = '*' * 8 + i[2][-3:]

            ind_sb = i[4].index('@')
            i[4] = i[4][0] + '*' * (ind_sb-1) + i[4][ind_sb:]
            f2.write(' '.join(i))