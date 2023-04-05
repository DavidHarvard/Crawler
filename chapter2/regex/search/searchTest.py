import re 

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra   stings'

result = re.search('Hello.*?(\d+).*?Demo',content)

print(result)

#在匹配时 search方法会一次以每个字符作为开头扫描字符串 直到找到第一个符合规则的字符串 然后返回匹配内容
# 如果没有找到符合规则的字符串 就返回None

#为了使匹配方便 尽量使用search方法


