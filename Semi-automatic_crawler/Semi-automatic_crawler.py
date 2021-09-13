import re
import csv

with open('source.txt', 'r', encoding='utf-8') as f:
    source = f.read()

result_list = []
username_list = re.findall('title="主题作者: (.*?)"', source, re.S)
content_list = re.findall('href="/p/.*?" title="(.*?)"', source, re.S)
create_list = re.findall('title="创建时间">(.*?)</span>', source, re.S)
print(username_list)
print(content_list)
print(create_list)
for i in range(len(username_list)):
    result = {'username': username_list[i],
              'content': content_list[i],
              'create_time': create_list[i]
              }
    result_list.append(result)

with open('HarryPotter_tieba.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['username','content','create_time'])
    writer.writeheader()
    writer.writerows(result_list)












