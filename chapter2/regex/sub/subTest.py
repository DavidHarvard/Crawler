import re 
content = '5453486434asdjk35456'

content = re.sub('\d+','',content)

print(content)


#当我们想要替换修改文本的时候可以使用replace方法 但是用这个方法过于繁琐 可以直接使用sub方法

