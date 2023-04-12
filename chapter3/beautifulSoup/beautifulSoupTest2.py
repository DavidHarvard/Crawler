html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#初始化beautifulsoup的时候对于不标准的html字符串就自动更正了格式
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
#调用prettify方法 这个方法可以将要解析的字符串以标准的缩进格式输出
print(soup.prettify())
print(soup.title.string)

