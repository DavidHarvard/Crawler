from urllib.parse import parse_qsl

query = 'name=germey&age=25'
print(parse_qsl(query))
#可以看到运行结果是一个列表 该列表中每一个元素都是一个元组 元组的第一个内容是参数名 第二个内容是参数值
