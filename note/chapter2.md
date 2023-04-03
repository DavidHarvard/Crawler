urlopen几个参数的用法{
    1.data : 需要用bytes方法将参数转化为字节流格式的内容 如果传递了这个参数 那么他的请求方式就是post请求
    2.timeout: 超时设置如果发给服务器的请求在设置的时间内没有返回值就报错
}
request有几个参数的用法{
    class urllib.request.Request(url,data=None,headers={},origin_req_host=None,unverifiable=False,method=None)
    1.第一个参数url是请求的url，这是必传的参数，其他的都是可选的参数
    2.第二个参数data是如果要传输数据，必须要传输bytes类型的。如果数据是字典，可以先用urllib.parse模块里的urlencode方法进行编码
    3.第三个参数header是一个字典：就是请求头 我们在构造请求时，既可以使用headers参数直接构造此项，也可以使用实例的add_header方法添加
    添加请求头最常见的方法就是通过修改user-Agent来伪装浏览器
    4.第四个参数origin_req_host指的是请求方的host名称或者ip地址
    5.第五个参数unverifiable表示的是是否是无法验证 默认值是False 意思是用户没有权限来接受这个请求的结果
    6.第六个参数method表的是请求的方法 例如;GET,POST
}