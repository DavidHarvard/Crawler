import re 
html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

## 想获取所有的歌曲的名字
##我们使用sub的方法来解决这个问题

##首先替换a标签

html = re.sub('<a.*?>|</a>','',html)
results = re.findall('<li.*?>(.*?)</li>',html,re.S)
for result in results:
    #strip() 方法不加参数的时候可以消除文本在前面后面的空白格 如果里面有参数(一个字符串) 就将文本中的这个参数的字符串删除掉
    print(result.strip())
