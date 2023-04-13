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

from parsel import Selector 

selector = Selector(text=html)
items = selector.css('.item-0')
for item in items:
    #get 方法的作用是SelectirList里面提取第一个Selector对象，然后输出其中的结果
    text = item.xpath('.//text()').get()
    print(text)
result = selector.xpath('//li[contains(@class,"item-0")]//text()').get()
print(result)

# result1 = selector.xpath('//li[contains(@class,"item-0")]//text()').getall()
# print(result1)
print("获取href属性")
href = selector.css('.item-0.active a::attr(href)').get()
print(href)

result = selector.xpath('//li[contains(@class,"item-0") and contains(@class,"active")]/a/@href').get()
print(result)

result = selector.css('.item-0').re('link.*')
print(result)