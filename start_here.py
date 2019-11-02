import pymongo
from pymongo import MongoClient

from settingSecret import MyMongoDBServerTest01

# GET CONNECTION STRING
cluster = MongoClient(MyMongoDBServerTest01.full_connection_string)

# CONNECT TO MongoDB DATABASE
db = cluster['test']
collection = db['user']

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

