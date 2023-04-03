#该方法将内容准话为URL编码的格式，然后当URL中带有中文参数的时候，有可能导致乱码问题，此时用quote方法可以将中文字符转化为URL编码
from urllib.parse import quote

keyword = '梅西'
url = 'https:www.baidu.com/s?wd='+ quote(keyword)
print(url)