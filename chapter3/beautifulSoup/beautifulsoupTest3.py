html = """
<html>
  <head>
    <title>The Dormouse's story</title>
  </head>
  <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">
      Once upon a time there were three little sisters; and their names were
      <a href="http://example.com/elsie" class="sister" id="link1"
        ><!-- Elsie --></a
      >,
      <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
      and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
    
  </body>
</html>
""" 
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.p)
#后面的几个p节点并没有选取到也就是说 当有多个节点时这种选择方式指挥选择到第一个匹配的节点后面的节点会忽略
print(soup.head)

print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])