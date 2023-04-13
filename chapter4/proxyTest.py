import requests
s = requests.session()
print('ssss')

url = "https://mail.163.com/"
s.keep_alive = False
s.proxies = {"https": "47.100.104.247:8080", "http": "36.248.10.47:8080", }
r = s.get(url)
print (r.status_code)  # 如果代理可用则正常访问，不可用报以上错误
print('ssss')