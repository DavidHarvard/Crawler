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
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup  = BeautifulSoup(html,'lxml')
#这里寻找的仅仅是a节点的直接父节点 而没有再向外寻找祖先节点
print(soup.a.parent)
#寻找所有的祖先节点
print(list(enumerate(soup.a.parents)))