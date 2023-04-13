import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient(host='localhost', port=27017)

# client = MongoClient('mongodb://localhost:27017/')

db = client.test
# db = client['test']

collection = db.students

results = collection.find_one({'name':'Mike'})
print(type(results))
print(results)

result = collection.find_one({'_id':ObjectId('6437c838260b9f2c59703cd2')})
print(result)

#查询多条数据 使用 find方法

results = collection.find({'age':20})
print(results)
for result in results:
    print(result)

#如果要查询age 大于20的数据

results = collection.find({'age':{'$gt':20}})

#统计有多少条
count = collection.estimated_document_count()
print(count)

# count = collection.find({'age': 20}).estimated_document_count()
print(count)

#排序 降序使用 pymongo.DESCENDING
results = collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])

#偏移也就是忽略几个元素
###值得注意的是 ，在数据库中数据量非常庞大的时候最好不要使用大偏移来查询数据，因为这样很可能导致内存溢出
results = collection.find().sort('name',pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])
##另外还可以使用limit方法指定要获取结果的个数
results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])
