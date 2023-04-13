import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
#通过loads方法将字典类型的数据转换为了json类型的数据
data = json.loads(str)
print(data)
print(type(data))