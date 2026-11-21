import numpy as np
import matplotlib.pyplot as plt

# --- Данные ---------------------------------------------------------------
year = {}

with open('movies.txt', 'r', encoding='utf-8') as f: 
    l = f.readline().replace("\n","")
    for i in f:
        # разбиение строки по разделителю
        j = i.replace("\n", "").split(";")
        y = j[1]
        r = float(j[3])

        if year.get(y, 0):
            year[y].append(r)
        else:
            year[y] = [r]

year = dict(sorted(year.items(), key=lambda item: item))
sr_y = [sum(i)/len(i) for i in year.values()]
year = list(year.keys())

mx = max(sr_y)
mx_y = year[sr_y.index(mx)]

sr_sr = sum(sr_y)/len(sr_y)

# # --- Построение ------------------------------------------------------------
# # Создание фигуры и диаграммы

fig, ax = plt.subplots(figsize=(15, 7))

ax.plot(year, sr_y,
        label='Средний рейтинг',
        color='lightcoral'
        )
ax.plot(mx_y, mx, 
        color='maroon', 
        marker='o',
        markersize=4)
ax.annotate(f'{mx_y}:{mx:.2f}',
        xy=(mx_y,mx), 
        xytext=(int(mx_y)-1990, mx+0.02),
        color='maroon',
        ha='center'
            )
ax.axhline(sr_sr, color='mediumseagreen')
ax.text(0, sr_sr-0.025, f'среднее: {sr_sr:.2f}',
        color='green')

ax.set_title('Средние рейтинги фильмов по годам')
ax.set_xlabel('Год')
ax.set_ylabel('Средний рейтинг')
ax.tick_params(axis='x', labelsize=8)
ax.grid(True)

fig.tight_layout()
plt.show()

