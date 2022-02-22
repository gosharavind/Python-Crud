import mongoDBmodule as MDB
# res = mongoDBmodule.db.create_collection('user')
# mongoDBmodule.createColletion()
# print(mongoDBmodule.insertOneColletion('sampleData',{
#     "name": "shanthi",
#     "age": 24
# }))
# print(mongoDBmodule.createColletion('products'))
print(MDB.readSingleDocQuery('sampleData'))