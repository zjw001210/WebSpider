import lxml.html

html1 = '''
<! DOCTYPE html>
<html>￼  
<head lang="en">￼      
    <meta charset="UTF-8">￼      
    <title></title>￼  
</head>￼  
<body>￼      
    <div id="test3">￼        
        我左青龙，￼        
        <span id="tiger">￼            
            右白虎，￼            
            <ul>上朱雀，￼                
                <li>下玄武。</li>￼            
            </ul>￼            
            老牛在当中，￼        
        </span>￼        
        龙头在胸口。￼      
    </div>￼  
</body>￼  
</html>
'''
# 只有“我左青龙”和“龙头在胸口”这两句是真正属于这个id = "test" <div>标签的文字信息。
# XPath并不会自动把子标签的文字提取出来。
# 在这种情况下，就需要使用string(.)关键字了。

# 首先像先抓大再抓小一样，
# 先获取<div id="test3">这个结点，但是不获取里面的东西。
# 接着对这个结点再使用一次XPath，提取整个结点里面的字符串。

# 使用string(.)关键字获取所有文本信息
selector = lxml.html.fromstring(html1)
data = selector.xpath('//div[@id = "test3"]')[0]
info = data.xpath('string(.)')
print(info)

