import requests

data = {'name':'david' , 'age' : '21'}

r = requests.post("https://www.httpbin.org/post",data=data)
print(r.text)