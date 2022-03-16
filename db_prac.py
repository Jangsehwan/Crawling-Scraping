from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbstudy

# db.users 콜렉션이름주위

# insert
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

# find
# user = db.users.find_one({'name':'bobby'}, {'_id':False})
# print(user['age'])

# update
# name이 bobby인 애를찾아서 age를 19로 update
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
# db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

# delete 거의 안써
# db.users.delete_one({'name':'bobby'})

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})