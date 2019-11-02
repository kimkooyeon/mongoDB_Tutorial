import pymongo
from pymongo import MongoClient

from settingSecret import MyMongoDBServerTest01

# GET CONNECTION STRING
cluster = MongoClient(MyMongoDBServerTest01.full_connection_string)

# CONNECT TO MongoDB DATABASE
db = cluster['test']
collection = db['user']

# GET TOTAL RECORDS
# total = collection.count_documents({})
# print(total)

# INSERT OPERATION
# test_user = {'_id':0, 'name':'kim', 'email':'xyz@test.com'}
# collection.insert_one(test_user)


# INSERT WITHOUT _ID
# test_user2 = {'name': 'kim2', 'email': '222@222.com'}
# collection.insert_one(test_user2)

# INSERT MANY
# test_user101 = {'_id':101, 'name':'kim101', 'email':'user101@test.com'}
# test_user102 = {'_id':102, 'name':'kim102', 'email':'user102@test.com'}
# collection.insert_many([test_user101, test_user102])

# FIND OPERATION
# if collection.count_documents({'name':'kim'}) > 0:
#     results = collection.find({'name': 'kim'})
#     for r in results:
#         print(r)
#         print(r['email'])

# FIND WITH MULTIPLE CRITERIA
# if collection.count_documents({'name':'kim', 'email':'xyz@test.com'}) > 0:
#     results = collection.find({'name': 'kim', 'email':'xyz@test.com'})
#     for r in results:
#         print(r)
#         print(r['email'])

# FIND ONE
# result1 = collection.find_one({'name': 'kim'})
# print(result1)
# print(result1['name'], result1['email'])

# FIND ALL
results = collection.find()
for r in results:
    print(r)
#     print(r['name'], r['email'])

# DELETE A RECORD
# result = collection.delete_one({'_id':0})
# print(result)

# DELETE ALL
# result = collection.delete_many({})
# print(result.deleted_count)

# UPDATE A RECORD
# result = collection.update_one(filter={'_id':0}, update={'$set':{'name':'kim'}})
# result = collection.update_one(filter={'name':'kim'}, update={'$set':{'name':'kkk'}})

# UPDATE A RECORD WITH NEW FIELD
# result = collection.update_one(filter={'_id':0}, update={'$set':{'address':'Singapore'}})

# UPDATE MANY RECORD
# result = collection.update_many(filter={}, update={'$set': {'contact': '65'}})

# UPDATE MANY RECORD WITH NEW FIELD
# result = collection.update_many(filter={}, update={'$set': {'address': 'Singapore'}})

