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

print(doc('#container .list li'))
print(type(doc('#container .list li')))

#获取文本内容

for item in doc('#container .list li').items():
    print(item.text())

items = doc('.list')
print(type(item))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

#获取所有子结点

kids = items.children()
print(type(kids))
print(kids)

#获取制定的节点

kid = items.children('.item-1')
print(type(kid))
print(kid)

#父节点
container = items.parent()
print(type(container))
print(container)

#查找祖先节点
parents = items.parents()
print(type(parents))
print("****")
#会返回所有的祖先节点
print(parents)

parent = items.parents('.wrap')
print(parent)

#兄弟节点


from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings())


