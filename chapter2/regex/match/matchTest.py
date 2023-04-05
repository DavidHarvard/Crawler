import re

content = "Hello 123 4567 World_This is a Regex demo"
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())
#开头的^表示匹配的字符串的开头,也就是以Hello开头 \S 表示匹配空白字符，用来匹配目标字符串里hello后面的空格；\d表示匹配数字，
#3个\d表示匹配三个数字123；紧接着的一个\s表示匹配空白字符；目标字符串后买你还有4567，我们其实可以依然使用4个\d来表示，但是
#这么些有一些繁琐，所以可以用\d后面跟{4}的形式表示匹配4此数字 后面又是一个空格所以又是一个\s
#最后的\w{10} 表示匹配10个字母及下划线。我们注意到后这里其实并没有把目标字符串匹配完，不过这样依然可以进行匹配，只是匹配结果短一点而已。
