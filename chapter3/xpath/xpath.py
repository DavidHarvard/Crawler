from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

#最后一个li标签是没有闭合的 但是etree模块自动修正了html文本

html = etree.HTML(text)
#因为/用于直接获取子结点 而ul下面没有直接的a子结点 只有li节点 所以无法获取任何匹配结果
result = html.xpath('//ul/a')
print(result)

html1 = etree.parse(text,etree.HTMLParser)
result1 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result1) 