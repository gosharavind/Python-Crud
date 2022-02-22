import pymongo

if __name__ == "__main__":
        
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    db = myclient['pydb']
    # collection = db['sample']
    # # find one document
    # one = collection.find_one()
    #print(one)
    # find one documents with query
    # queryOne = collection.find_one({'name':"santh"})
    # print(queryOne)

    # find all Docs
    # allDocs = collection.find()
    # for item in allDocs:
    #     print(item)
    # find  Docs with specific fileds
    # allDocsWithQuery = collection.find({},{'name':1,'_id':0})
    # for item in allDocsWithQuery:
    #     print(item)    

    if(db.list_collection_names()==[]):
        collection = db['sample']
        dictionary = {'name':'santh','age':29}
        collection.insert_one(dictionary)
    