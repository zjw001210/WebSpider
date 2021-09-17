import lxml.html

source = '''
<html>
    <head>
        <title>测试</title>
    </head>
    <body>
        <div class="useful">
            <ul>
                <li class="info">我需要的信息1</li>
                <li class="info">我需要的信息2</li>
                <li class="info">我需要的信息3</li>
            </ul>
        </div>
        <div class = "useless">
            <ul>
                <li class = "info">垃圾1</li>
                <li class = "info">垃圾2</li>
            </ul>
        </div>
    </body>
</html>         
'''
selector = lxml.html.fromstring(source)
useful = selector.xpath('//div[@class = "useful"]')
info_list = useful[0].xpath('ul/li/text()')

useless = selector.xpath('//div[@class = "useless"]')
useless_list = useless[0].xpath('ul/li/text()')
# 在对XPath返回的对象再次执行XPath的时候，
# 子XPath开头不需要添加斜线，直接以标签名开始即可
print(useful, '\n', useless)
print(info_list)
print(useless_list)

