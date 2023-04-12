html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
import os
from pyquery import PyQuery as pq
doc = pq(html)

print(doc('li'))

doc1 = pq(url='https://cuiqingcai.com')
print(doc1('title'))

doc = pq(filename='/home/david/桌面/Crawler/chapter3/pyquery/demo.html')
print(doc('li'))
basedir = os.path.dirname(__file__)
print("basedir:" + basedir)