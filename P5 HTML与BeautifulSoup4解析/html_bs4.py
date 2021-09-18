import re
from bs4 import BeautifulSoup
import requests
import lxml

source = requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()

print('-------------------------------')
print('source:\n', source)
print('-------------------------------')

# 1.解析源代码生成BeautifulSoup对象：
# 可以用html.parser来解析
soup = BeautifulSoup(source, 'html.parser')
# 或者可以用lxml来解析
soup_2 = BeautifulSoup(source, 'lxml')

# 2.查找内容

# 2.1 用find()
# 由于HTML中的class属性与Python的class关键字相同，
# 因此为了不产生冲突，BS4规定，如果遇到要查询class的情况，使用“class_”来代替：
info_1 = soup.find(class_='useful')  # 返回None
info_2 = soup.find(class_='test')
info_3 = soup_2.find(class_='useless')  # 返回None
info_4 = soup_2.find(class_='info')
print('返回对象类型：', type(info_1), type(info_3))
print(info_1.string, info_2.string, info_3.string, info_4.string)
print('-------------------------------')

# 2.2 用find_all(name, attrs, recursive, text, **kwargs)
# name就是HTML的标签名，类似于body、div、ul、li
# attrs参数的值是一个字典，字典的Key是属性名，字典的Value是属性值
attrs = {'class': 'useful'}
# recursive的值为True或者False，当它为False的时候，BS4不会搜索子标签。
# text可以是一个字符串或者正则表达式，用于搜索标签里面的文本信息。

content = soup.find_all(text=re.compile('我需要'))
print('用re来find_all:')
for each in content:
    print(each.string)
print('-------------------------------')
# **kwargs表示Key=Value形式的参数。这种方式可以根据属性和属性值进行搜索。
# Key是属性，Value是属性值。
'''
find_all('div', id = 'test')
find_all(class_='iamstrange')
'''
# 用正则表达式：
'''
content = soup.find_all(class_=re.compile('iam'))
for each in content:
    print(each.string)
'''

# 先用find()再用find_all()，先抓大再抓小
info_useful = soup.find('div', attrs=attrs, recursive=True)
info_5 = info_useful.find_all('li')
print('info_5: ')
for i in info_5:
    print(i.string)

# 将BS Tag对象看作字典，将属性名当作Key，获取属性值
useful = soup.find(class_='useful')
all_content = useful.find_all('li')
# 打印完整信息
for li in all_content:
    print(li)
# 打印Value
for li in all_content:
    print(li.string)
# 打印Key
for li in all_content:
    print(li['class'])



