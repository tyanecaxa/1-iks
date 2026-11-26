with open("files/server_log.txt", 'r', encoding='utf-8') as f1:
    # st = []
    inf = 0
    warn = 0
    er = 0
    crit = 0
    for i in f1:
        # i = i.replace('\n','').split(maxsplit=3)
        # st.append(i)

        if "INFO" in i:
            inf += 1
        if "WARNING" in i:
            warn += 1
        if "ERROR" in i:
            er += 1
        if "CRITICAL" in i:
            crit += 1

    # print(st)
print(f"INFO: {inf}")
print(f"WARNING: {warn}")
print(f"ERROR: {er}")
print(f"CRITICAL: {crit}")