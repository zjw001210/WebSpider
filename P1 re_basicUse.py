# 正则表达式re
import re

content = "我的微博密码是：1234567，QQ密码是：33445566，银行卡密码是：888888，Github密码是：999abc999，帮我记住它们"
# 1.method:.findall
password_list = re.findall('：(.*?)，', content)
name_list = re.findall('名字是：(.*?)，', content)
print('找到内容，返回：{}'.format(password_list))
print('找不到任何内容，返回：{}'.format(name_list))

print('\n')

# 2.method:search
password_search = re.search('密码是：(.*?)，', content)
password_search_not_find = re.search('xxx：(.*?)，', content)
print('password_search: ', password_search)
print('password_search_g0: ', password_search.group(0))
print('password_search_g1: ', password_search.group(1))
print('password_search_not_find: ', password_search_not_find)
# 下面这2句会报错：'NoneType' object has no attribute 'group'
# print('password_search_not_find_g0: ', password_search_not_find.group(0))
# print('password_search_g1: ', password_search_not_find.group(1))

account_content = "微博账号是：kingname，密码是：1234567，QQ账号是：9999，密码是：33445566，银行卡账号是：00001，卡密码是：888888，帮我记住它们"
account_password = re.search('账号是：(.*?)，密码是：(.*?)，',account_content)
print('读取第一个括号的内容：{}'.format(account_password))
print('读取第一个括号的内容_g0：{}'.format(account_password.group(0)))
print('读取第一个括号的内容_g1：{}'.format(account_password.group(1)))
print('读取第一个括号的内容_g2：{}'.format(account_password.group(2)))

print('\n')

# 3.the difference between .* and .*?
without_question_mark = re.findall('密码是：(.*)，', content)
with_question_mark = re.findall('密码是：(.*?)，', content)
print('不使用问号的结果：{}，长度为：{}'.format(without_question_mark, len(without_question_mark)))
print('使用问号的结果：{}，长度为：{}'.format(with_question_mark, len(with_question_mark)))

# 4.fist process valid, then invalid 先抓大再抓小
big_small_text = '''
有效用户：
姓名：张三
姓名：李四
姓名：王五
无效用户：
姓名：不知名的小虾米
姓名：隐身的张大侠
'''
user = re.findall('姓名：(.*?)\n', big_small_text)
print("有效内容与无效内容混淆：", user)
new_text = re.findall('有效用户：(.*?)无效用户', big_small_text, re.S)
print(new_text)
user2 = re.findall('姓名：(.*?)\n', new_text[0]) # 一定要是字符串，而不是列表
print("获取有效内容：", user2)

# 5.inner and outer of the bracket 括号内外都可以有字符
html = '''<div class="tail-info">客户端</div>
<dic class="tail-info">2017-01-01 13:45:00</div>
'''
result1 = re.findall('tail-info">(.*?)<', html)
result2 = re.findall('tail-info">(2017.*?)<', html)
print("2017在括号外：{}".format(result1))
print("2017在括号里：{}".format(result2)) # 更精准定向
