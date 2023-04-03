import requests
from requests.packages import urllib3
# response = requests.get('https://ssr2.scrape.center/')
# print(response.status_code)
#抛出了SSLError，原因是我们请求的URL的证书是无效的

#我们可以通过设置忽略警告忽略ssl证书的警告
response = requests.get('https://ssr2.scrape.center/',verify = False)
print(response.status_code)
#我们可以通过设置忽略警告
urllib3.disable_warnings()
response = requests.get('https://ssr2.scrape.center/',verify = False)
print(response.status_code)