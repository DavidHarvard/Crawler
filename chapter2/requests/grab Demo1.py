import requests
import re
import urllib3
urllib3.disable_warnings()
r = requests.get('https://ssr1.scrape.center/',verify=False)
pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
title = re.findall(pattern,r.text)
print(title)