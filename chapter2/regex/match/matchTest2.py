import re

cotent = 'Hello 1234567 World This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld',cotent)

print(result)
print(result.group())
print(result.group(1))
print(result.span())
#这里的group(1),它与group()不同 后者会输出一个完整的匹配结果 前者会输出一个被()包围的匹配结果

r = re.match('^Hello.*Demo$',cotent)

print(r)
print(r.group())
print(r.span)