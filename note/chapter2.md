urlopen 几个参数的用法{
1.data : 需要用 bytes 方法将参数转化为字节流格式的内容 如果传递了这个参数 那么他的请求方式就是 post 请求
2.timeout: 超时设置如果发给服务器的请求在设置的时间内没有返回值就报错
}
request 有几个参数的用法{
class urllib.request.Request(url,data=None,headers={},origin_req_host=None,unverifiable=False,method=None) 1.第一个参数 url 是请求的 url，这是必传的参数，其他的都是可选的参数 2.第二个参数 data 是如果要传输数据，必须要传输 bytes 类型的。如果数据是字典，可以先用 urllib.parse 模块里的 urlencode 方法进行编码 3.第三个参数 header 是一个字典：就是请求头 我们在构造请求时，既可以使用 headers 参数直接构造此项，也可以使用实例的 add_header 方法添加
添加请求头最常见的方法就是通过修改 user-Agent 来伪装浏览器 4.第四个参数 origin_req_host 指的是请求方的 host 名称或者 ip 地址 5.第五个参数 unverifiable 表示的是是否是无法验证 默认值是 False 意思是用户没有权限来接受这个请求的结果 6.第六个参数 method 表的是请求的方法 例如;GET,POST
}

(没有内容不可以使用.\*?查询)

只要是写正则表达式就应该加上 re.S 分行查询
