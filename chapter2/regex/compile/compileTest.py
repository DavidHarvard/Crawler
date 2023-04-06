import re

content1 = '2019-12-25 12:00'
content2 = '2019-12-17 12:55'
content3 = '2022-4-11  13:44'


pattern = re.compile('\d{2}:\d{2}')
result = re.sub(pattern ,'',content1)
result = re.sub(pattern ,'',content2)
result = re.sub(pattern ,'',content3)
print(result)

#没有必要重复写3个一样的正则表达式所以可以借助 compile来将正则表达式编译成一个对象 以便复用

#另外在compile中可以传入修饰符 例如 re.S等修饰符 这样在findall 和search方法中就不需要额外传了