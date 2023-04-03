from urllib.parse import parse_qs

query = 'name=germey&age=25'
print(parse_qs(query))
#反序列化，利用parse_qs方法，可以将一串GET请求参数转回字典
