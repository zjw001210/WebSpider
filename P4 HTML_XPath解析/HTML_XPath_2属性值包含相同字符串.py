import lxml.html

html1 = ''''
<! DOCTYPE html>
<html>￼
<head lang="en">￼
    <meta charset="UTF-8">￼
    <title></title>                     
</head>
<body>
<div id="abc-key-1">需要的内容1</div>        
<div id="123-key-2">需要的内容2</div>
<div id="haha-key-hh">需要的内容3</div> 
<div id="useless">这是我不需要的内容</div>
</body>   
</html>
'''
selector = lxml.html.fromstring(html1)
content = selector.xpath('//div[contains(@id, "key")]/text()')
for item in content:
    print(item)

