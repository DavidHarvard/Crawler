import requests
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text[:100])
print(r.cookies)


data = {
    'name':'david',
    'age' : '21'
}

a = requests.get('https://www.httpbin.org/get',params=data)
print(type(a.text))
print(a.text)
print(a.json())
print(type(a.json()))