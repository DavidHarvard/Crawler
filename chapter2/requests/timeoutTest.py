import requests
#使用timeout参数来设置超时时间 timeout用作为timeout的总和
r = requests.get('https://www.baidu.com' , timeout = 1)
print(r.status_code)
#如果分别制定用作连接和读取的timeout，则可以传入一个元组：
r = requests.get('https://www.taobao.com', timeout = (5,30))
print(r.status_code)