#爬去网站首页10部电影的数据 然后将相关星系存储为txt文本格式

import requests
from pyquery import PyQuery as pq
import re
import urllib3


urllib3.disable_warnings()
url = 'https://ssr1.scrape.center/'
html =  requests.get(url,verify=False).text
doc = pq(html)
items = doc('.el-card').items()

file = open('/home/david/桌面/Crawler/chapter4/saveTxt/movie.txt','w',encoding='utf-8')

for item in items:
    #电影名称
    name = item.find('a > h2').text()
    file.write(f'类别 :{name}\n')
    #类别
    categories = [item.text() for item in item.find('.categories button span').items()]
    file.write(f'类别：{categories}\n')
    #上映时间
    published_at = item.find('.info:contains(上映)').text()
    #此时的\是作为续行符号出现的 此时下面两行额的demo此时就是一行代码
    published_at = re.search('(\d{4}-\d{2}-\d{2})',published_at).group(1) \
    if published_at and re.search('(\d{4}-\d{2}-\d{2})',published_at) else None
    file.write(f'上映时间：{published_at}\n')


    #评分
    score = item.find('p.score').text()
    file.write(f'评分：{score}\n')
    file.write(f'{"=" * 50}\n')
    file.close
