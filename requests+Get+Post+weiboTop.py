import requests
import re

# 用get方法访问
html_str = requests.get('https://s.weibo.com/top/summary/').content.decode()
print(html_str)
print('--------------------------')

# 用post方法访问
data = {'name': 'kingname', 'password': '1234567'}
html_formdata = requests.post('http://exercise.kingname.info/exercise_requests_post', data=data)
print(html_formdata.content.decode())
print('--------------------------')
html_formdata = requests.post('http://exercise.kingname.info/exercise_requests_post', json=data)
print(html_formdata.content.decode())

# 用正则表达式解析weibo热搜
content_result = []
title = re.search('<title>(.*?)</title>', html_str, re.S)
content = re.findall('<a href=".*?=top" target="_blank">(.*?)</a>', html_str, re.S)
for i in range(len(content)):
    item = str(i+1) + content[i]
    content_result.append(item)
print(f'页面标题：\n{title.group(1)}')
print('页面正文内容：')
for i in range(len(content_result)):
    print(content_result[i])







