from selenium import webdriver

# 创建 Chrome 浏览器驱动对象
driver = webdriver.Chrome()

# 目标网页url
url = 'http://192.168.0.156:9011/'

# 发送请求并打开网页
test = driver.get(url)

# 使用 JavaScript path 定位目标元素
# target_element = driver.find_element_by_js('return document.querySelector("#menu-block-right-container > div > div.ant-tabs-content > div > div > div > div:nth-child(2) > div > div > div.ant-spin-container > div > div > div.ant-table-fixed-right > span > div > div > table > tbody > tr:nth-child(9) > td:nth-child(4)")')

# # 获取目标元素的文本内容
# target_text = target_element.text

# 输出目标文本内容
print(test)

# 关闭浏览器驱动对象
driver.quit()
