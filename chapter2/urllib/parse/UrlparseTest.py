from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
#返回ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
#：前面的内容就是scheme，代表协议
#：第一个/前面便是netloc，代表域名
#：path 代表访问路径
#：params 代表参数
#：问好？后面是查询条件query 一般用作GET类型的URL 
#：#后面是锚点fragment 用于直接定位页面内部的下拉位置
