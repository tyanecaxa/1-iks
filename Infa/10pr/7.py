import json

with open('files/servers.json', 'r', encoding='utf-8') as f:
    s = json.load(f)
    on = 0
    of = 0
    fo = []
    ma = 0
    for i in s:
        if s[i] == 'online':
            on += 1
        if s[i] == 'offline':
            of += 1
            fo.append(i)
        if s[i] == 'maintenance':
            ma += 1
    print(f'online: {on}, offline: {of}, maintenance: {ma}')
    print('offline:')
    for i in fo:
        print(i)
        