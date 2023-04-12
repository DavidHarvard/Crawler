html = '''
<div class="wrap">
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
 </div>
'''
from pyquery import PyQuery as pq

doc = pq(html)

a = doc('.item-0.active a')
print(a,type(a))
print(a.attr('href'))

#遍历获取属性
b = doc('a')
for item in b.items():
    print(item.attr('href'))

#获取文本
print(a.text())
# text方法可以返回多个同样节点(eg:div)的内部纯文本 但是html知识返回字符串
