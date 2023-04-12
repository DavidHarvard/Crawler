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
#所以说addClass 和 removeClass可以动态改变节点class的属性

from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)


li.attr('name','link')
print(li)
#将全部的文本全被改为传入的字符串文本
li.text('changed item')
print(li)
#将全部的文本全被改为传入的html
li.html('<span>changed item</span>')
print(li)