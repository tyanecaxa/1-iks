with open("files/server_log.txt", "r", encoding='utf-8') as f1:
    with open("files/errors_only.txt", 'w', encoding='utf-8') as f2:
        x = 0
        for i in f1:
            if "ERROR" in i or "CRITICAL" in i:
                x += 1
                f2.write(i)
print(f"Найдено {x} критических ошибок")

# 521