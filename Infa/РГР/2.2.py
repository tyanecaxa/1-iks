import numpy as np
import matplotlib.pyplot as plt

# --- Данные ---------------------------------------------------------------
# 1
imdb = {}
# 2
genre = {}

with open('movies.txt', 'r', encoding='utf-8') as f: 
    l = f.readline().replace("\n","")
    for i in f:
        # разбиение строки по разделителю
        j = i.replace("\n", "").split(";")
        j[3] = float(j[3])

        if imdb.get(str(j[3]), 0):
            imdb[str(j[3])] += 1
        else:
            imdb[str(j[3])] = 1

        if genre.get(j[2],0):
            genre[j[2]] += 1
        else:
            genre[j[2]] = 1
sort_imdb = dict(sorted(imdb.items(), key=lambda item: item[1], reverse=True))
sort_genre = dict(sorted(genre.items(), key=lambda item: item[1], reverse=True))

imdb = list(sort_imdb.keys())
len_imdb = list(sort_imdb.values())

genre = list(sort_genre.keys())
len_genre = list(sort_genre.values())

# --- Построение ------------------------------------------------------------
# Создание фигуры и диаграммы

fig, ax = plt.subplots(figsize=(10, 5))

ax.barh(genre[:10], len_genre[:10],
        label='Количество фильмов',
        color='lightcoral',
        edgecolor='maroon')
ax.invert_yaxis()

ax.set_title('Топ-10 жанров по количеству фильмов')
ax.set_xlabel('Количество фильмов')
ax.set_ylabel('Жанр')
ax.tick_params(axis='x', labelsize=8)
ax.legend()

fig.tight_layout()
plt.show()

