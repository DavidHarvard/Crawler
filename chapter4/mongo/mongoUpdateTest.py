import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

# client = MongoClient('mongodb://localhost:27017/')

db = client.test
# db = client['test']

collection = db.students

condition = {'name': 'Mike'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update_one(condition, student)
print(result)