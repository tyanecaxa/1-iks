def no_punctuaytia(l):
    l = l.replace(".", '')
    l = l.replace(",", '')
    l = l.replace("!", '')
    l = l.replace("?", '')
    l = l.lower()
    return l

with open("files/article.txt", 'r', encoding='utf-8') as f:
    l = f.readline()
    sl = {}
    l = no_punctuaytia(l)

    st = l.split(" ")
    while "" in st:
        st.remove("") 

    for i in st:
        if sl.get(i, 0):
            sl[i] += 1
        else:
            sl[i] = 1

    sl = sorted(sl.items(), key=lambda x: x[1], reverse=True)
    for s,c in sl[:5]:
        print(s, c)


    
    