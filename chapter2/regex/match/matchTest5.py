import re

content = '''Hello 1234567 World_This 
is a Regex Demo'''
result = re.match('^He.*?(\d+).*Demo$',content,re.S)

print(result.group(1))

# 因为.*?是匹配除了换行符之外的所有任意字符当遇到换行符的时候就不匹配了 导致匹配失败
#所以这里只需要加上一个修饰符re.S 就可以修正这个错误
