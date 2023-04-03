from urllib.parse import urlencode

params ={
    'name' : 'germey',
    'age' : 25
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
#参数成功的由字典类型转化为GET请求参数
#urlencode方法非常常用 有时为了方便的构造参数 我们会实现用字典将参数表示出来 然后将字典转化为URL的参数时，只需要调用该方法即可