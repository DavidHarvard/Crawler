# 完成的目标：
# 1.利用request爬去这个站点的每一页的电影列表，顺着列表再爬去每个电影的详情页
# 2.用正则表达式爬去每部电影的名称，封面，类别，上映时间，评分，剧情简介等内容
# 3.爬去的内容保存为json文本文件
# 4.使用多进程实现爬取的加速 


# 首先完成构造10页索引页url 分析提取出每个电影的详情页url

import requests
import logging #输出信息
import re 
from urllib.parse import urljoin  #拼接url
import json
from os import makedirs
from os.path import exists
import multiprocessing


#将数据保存到文件夹RESULTS_DIR 然后判断文件夹是否存在 如果不存在就创建一个
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


#定义一些基础变量
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')
BASE_URL = 'HTTPS://ssr1.scrape.center'
TOTAL_PAGE = 10

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

def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern,html)
    #如果items为空那么直接返回空列表
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL,item)
        logging.info('get deatil url %s',detail_url)
        yield detail_url

def scrape_detail(url):
    return scrape_page(url)

#解析封面 名称 类别 上映时间 评分 剧情简介
def parse_detail(html):
    #封面的正则表达式
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover"',re.S)
    #名字的正则表达式
    name_pattern = re.compile('<h2.*?class="m-b-sm">(.*?)</h2>')
    #类别的正则表达式
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>',re.S)
    #上映时间的正则表达式
    published_time_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    #评分的正则表达式 
    # <p data-v-63864230="" class="score m-t-md m-b-n-sm">9.5</p>
    point_pattern = re.compile('<p.*?class="score.*?".*?>(.*?)</p>',re.S)
    #剧情简介的正则表达式 (没有内容不可以使用.*?查询)
    description_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>',re.S)

    cover = re.search(cover_pattern,html).group(1).strip()  if re.search(cover_pattern,html) else None
    name = re.search(name_pattern,html).group(1).strip() if re.search(name_pattern,html) else None
    categories = re.findall(categories_pattern,html) if re.search(categories_pattern,html) else []
    published_time = re.search(published_time_pattern,html).group(1).strip() if re.search(published_time_pattern,html) else None
    point = re.search(point_pattern,html).group(1).strip() if re.search(point_pattern,html) else None
    description = re.search(description_pattern,html).group(1).strip() if re.search(description_pattern,html) else None
    #以字典的形式返回
    return {
        'cover' : cover,
        'name'  : name,
        'categories'  : categories,
        'published_time'  : published_time,
        'point' : point,
        'description'   : description
    }

#保存函数的编写
def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data,open(data_path,'w',encoding='utf-8'),
              ensure_ascii=False,indent=2)




def main(page):
    for page in range(1 , TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info("get detail data %s", data)
            logging.info("data saved successfully")
            save_data(data)
            logging.info('data saved successfully')

#多进程处理
if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1,TOTAL_PAGE + 1)
    pool.map(main,pages)
    pool.close()
    pool.join()
