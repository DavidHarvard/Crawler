from urllib import request,error
import socket
# 这一种不捕获错误的写法会直接报错502
# response = request.urlopen('http://davidharvard.com')
# print(response)

try:
    response = request.urlopen('http://cuiqicai.com/404',timeout = 1)
except error.URLError as e:
    if(isinstance(e.reason , socket.timeout)):
        print('TIME OUT')
    print(e.reason)
#程序没有直接报错 而是输出了错误原因 这样可以避免程序异常终止 同时异常得到了有效处理