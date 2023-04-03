from urllib import request,error

try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
#因为 URLError时HTTPError的父类，所以选择先捕获子类的错误，再捕获父类的错误
# 先捕获HTTPError 获取它的错误原因，状态码，请求头等信息 如果不是HTTPError异常
# 就会捕获到URLError异常 然后输出错误原因。最后用else语句来处理正常的逻辑。
# 这是一个较好的异常处理写法    
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
#有时候reason属性返回的不一定时字符串 也可能是一个对象

try:
    response = urllib.requsest.urlopen('https://www.baidu.com',timeout=0.01)
except:
    urllib.error.URLEoor