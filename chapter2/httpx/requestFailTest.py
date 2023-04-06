import requests

url = 'https://spa16.scrape.center/'
response = requests.get(url)
print(response.text)
#有的网站会检测请求使用的是不是ython2.0 如果不是就拒绝返回任何结果 所以 requests库是使用HTTP/1.1去访问的个人网站
