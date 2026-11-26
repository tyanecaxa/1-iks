import json

playlist =  {}
with open("files/playlist.json",'r',encoding='utf-8') as f:
    playlist = json.load(f)
print(f'Жанры: {', '.join(playlist.keys())}')


print()
print("Какой жанр желаете послушать?")
user_genre = input()
while user_genre not in playlist.keys() and user_genre != 'ВЫХОД':
    print("Простите, но такого жанра нет")
    print("Попробуйте снова или напишите ВЫХОД")
    user_genre = input()

if user_genre in playlist.keys():
    print(f'Песни жанра {user_genre}:')
    for i in playlist[user_genre]:
        print(i)


print()
print("Добавлен файл новой песни. Как его записать?")
print("Формат: Исполнитель - название")
new_song = input()

while ('-' not in new_song or new_song.count('-') > 1) and new_song != 'ОТМЕНА':
    print()
    print("Пожалуйста, запишите исполнителя и название по указаному формату")
    print("Если в названии песни есть тире, используйте нижнее подчёркивание")
    print("Если вы не хотите наименовывать файл, напишите ОТМЕНА")
    print("Он назовётся по умолчанию Unknown - song {n}")
    new_song = input()
    
if new_song == 'ОТМЕНА':
    new_song = 'Unknown - song {n}'


print()
print("Какого она жанра?")
user_genre = input()
if user_genre.strip() == '':
    print('Ах! Как это нет жанра? Ну ладно...')
    user_genre = 'Прочие'

if playlist.get(user_genre, 0):
    playlist[user_genre].append(new_song)
else:
    playlist[user_genre] = [new_song]

with open('files/playlist.json','w',encoding='utf-8') as f:
    json.dump(playlist, f, ensure_ascii=False, indent=4)


