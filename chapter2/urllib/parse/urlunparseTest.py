from urllib.parse import urlunparse
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))
#成功实现了URL的构造