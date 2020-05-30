from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('127.0.0.1', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

all_users = list(db.users.find())

same_ages = list(db.users.find({'age':21}))

print(all_users[0]['name'])
for user in all_users:
    print(user)

user = db.users.find_one({'name':'bobby'})
print(user)

user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print(user)

db.users.delete_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'})
print(user)