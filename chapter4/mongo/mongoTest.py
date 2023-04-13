import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)

# client = MongoClient('mongodb://localhost:27017/')

db = client.test
# db = client['test']

collection = db.students
# collection = db['students']


student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
#需要将insert方法修改成 insert_one方法
result = collection.insert_one(student)
print(result)

student1= {
    'id': '20170122',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2= {
    'id': '20170102',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
#插入多个数据方法名字为insert_many
result = collection.insert_many([student1,student2])
print(result)