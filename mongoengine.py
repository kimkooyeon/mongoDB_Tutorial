from mongoengine import *

from settingSecret import MyMongoDBServerTest01

connect('test', )

# me.connect(MyMongoDBServerTest01.full_connection_string)

# DEFINE DOCUMENTS
class User(me.Document):
    username = me.StringField()
