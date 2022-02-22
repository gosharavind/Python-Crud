import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['sampleDB']

# to create a collection
def createColletion(colllection_name):
    doc = db.create_collection(colllection_name)
    return doc

# to insert data into a collecion
def insertOneColletion(colllection_name,data):
    doc = db.get_collection(colllection_name).insert_one(data)
    return doc

# to insert Many docs into a collecion
def insertManyInColletion(colllection_name,data):
    docs = db.get_collection(colllection_name).insert_many(data)
    return docs

# to read a collection
def readColletion(colllection_name):
    docs = db.list_collection_names(colllection_name).find()
    for doc in docs:
        return doc

# to read single doc a collection
def readSingleDocQuery(colllection_name):
    docs = db.colllection_name.find_one()
    return docs