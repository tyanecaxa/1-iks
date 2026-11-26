import json

with open('files/movies.json','r',encoding='utf-8') as f:
    sp = json.load(f)

    database = sp['database_name']
    print(database)

    movies = sp['movies']
    count_movies = len(movies)
    print(count_movies)

    first_film = movies[0]
    print(first_film['title'], first_film['year'])

    sort_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)

    for i in sort_movies[:5]:
        print(f'[{i['title']}] ([{i['year']}]) - {i['rating']}: [{i['rating']}]')
