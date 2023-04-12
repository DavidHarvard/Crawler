html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
#contents 是返回的直接子节点组成的列表
print(soup.p.contents)

#children 返回的是生成器类型 
print(soup.p.children)
for i,child in enumerate(soup.p.children):
  print (i,child)

#返回所有的子孙节点 这次的输出结果就包含了span节点 因为descendants会递归查询所有子结点得到所有的子孙节点
print(soup.descendants)
for i,child in enumerate(soup.p.descendants):
  print(i,child)