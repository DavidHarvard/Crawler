import re

content = 'Hello 1234567 World This is a Regex Demo'
#这里只给匹配了一个数字7 因为 .*在贪婪匹配下会匹配尽可能多的字符。后面是\d+
#没有具体说明是几个字符所以就只给\d+留了一个数字7
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))

#我们也可以使用非贪婪匹配的写法.*?比贪婪匹配多一个？

r = re.match('^He.*?(\d+).*Demo$',content)
print(r)
print(r.group(1))
#所以说在做匹配的时候，字符串中间尽量使用.*?代替.?以免出现匹配结果缺失的情况
#但是我们需要注意的是如果匹配的结果在字符串的结尾 .*?就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符

src = "https://www.baidu.com/search/messi"

a = re.match('^https.*?search/(.*?)',src)
b = re.match('^https.*?search/(.*)',src)

print('result1',a.group(1))
print('result2',b.group(1))