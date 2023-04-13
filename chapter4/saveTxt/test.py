import requests
from pyquery import PyQuery as pq
import re
import urllib3

urllib3.disable_warnings()

url = 'https://static1.scrape.center/'
html = requests.get(url,verify=False)

# html = requests.get(url).text
# doc = pq(html)
# items = doc('.el-card').items()