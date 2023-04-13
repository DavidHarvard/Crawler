import json


#load方法是将整个文件中的内容转化为json对象 而loads可以灵活的控制要转化哪些内容

data = [{
    'name': '王位',
    'gender': 'male',
    'birthday': '1992-10-18'
}]


with open('/home/david/桌面/Crawler/chapter4/json/data.json', 'a', encoding='utf-8') as file:
    file.write(json.dumps(data))

with open('/home/david/桌面/Crawler/chapter4/json/data.json', 'a', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2))

with open('/home/david/桌面/Crawler/chapter4/json/data.json', 'a', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))