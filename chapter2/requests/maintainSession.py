import requests

#两次get是完全独立的操作对应两个完全不相关的session 那么第二次的访问就是不能拿到第一次已经设置好的cookies
requests.get('https://www.httpbin.org/cookies/set/number/123456789')
r = requests.get('https://www.httpbin.org/cookies')
print(r.text)


s = requests.Session()
s.get('https://www.httpbin.org/cookies/set/number/123456789')
r = s.get('https://www.httpbin.org/cookies')
print(r.text)
#利用session可以模拟一个会话而不用担心cookie的问题，它通常在模拟登录成功之后，精选下一步操作