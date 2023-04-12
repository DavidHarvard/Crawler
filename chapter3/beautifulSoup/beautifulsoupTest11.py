import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
#返回所有匹配正则表达式的信息
print(soup.find_all(text=re.compile('link')))