from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client.dbsparta 

target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))
for movie in movies:
    print(movie['title'])

