import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['sampleDB']
if(db.list_collection.count_documents()==[]):
    collection = db['sampleData']
    dictionary = {'name':'santh','age':29}
    collection.insert_one(dictionary)
    