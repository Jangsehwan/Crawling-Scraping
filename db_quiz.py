from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbstudy

target = db.movies.find_one({'title':'매트릭스'})
target_point = target['point']


target_movies = list(db.movies.find({'point':target_point},{'_id':False}))
# print(target_movies)
for target in target_movies:
    print(target['title'])


# db.movies.update_one({'title':'매트릭스'},{'$set':{'point':'0'}})