import requests
import re
import logging


def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get valid status code %s while scraping %s',response.status_code,url)
    except requests.RequestException:
        #我们将logging库中error方法里的exc_info参数设置为True 可以打印出Traceback错误堆栈的信息
        logging.error('error occurred while scraping %s',url,exc_info = True)


html  = scrape_page('https://ssr1.scrape.center/detail/1')
name_pattern = re.compile('<h2.*?class="m-b-sm">(.*?)</h2>')
name = re.search(name_pattern,html).group(1).strip() if re.search(name_pattern,html) else None
cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover"',re.S)
cover = re.search(cover_pattern,html).group(1).strip()  if re.search(cover_pattern,html) else None
categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>',re.S)
categories = re.findall(categories_pattern,html) if re.search(categories_pattern,html) else []
published_time_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
published_time = re.search(published_time_pattern,html).group(1).strip() if re.search(published_time_pattern,html) else None
point_pattern = re.compile('<p.*?class="score.*?".*?>(.*?)</p>',re.S)
point = re.search(point_pattern,html).group(1).strip() if re.search(point_pattern,html) else None
description_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?).*?</p>',re.S)
description = re.search(description_pattern,html).group(1).strip() 
print(description)