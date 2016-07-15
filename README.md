# 说明
爬虫程序运行请参考PDF，抓取豆瓣的大部分图书。包括抓取分类标签页，列表页，详情页并保存进数据库。

>A project for catch the book of 豆瓣website in china.
>please see the code source

#BUG
>2016.7.15修复标签页首页豆瓣改版
>及  Excel库函数API变化

# 目录结构

```
本爬虫程序目录如下：
----book  抓取的图书详情页
  　----文学　　　 大分类
  　　　----1000121昆虫记.html 标号+标题
    ----文化
    ----生活
    ----流行
    ----经管

----books 提取的图书列表页
  　----文学　　　 大分类
  　　　----茨威格.xlsx  标签
    ----文化
    ----生活
    ----流行
    ----经管

----data  提取的数据库文件
    ----doubanbook.book.sql  图书基本信息
    ----doubanbook_booktag.sql 图书标签信息

----image　抓取的图片
----img 实例图片

----web  抓取的图书列表页
  　----文学　　　 大分类
  　　　----茨威格  标签
              ----0.html  列表页
			  ----1.html
    ----文化
    ----生活
    ----流行
    ----经管
    ----book.html　　　测试的图书详情页
    ----books.html　　测试的图书列表页
    ----booktag.html　测试图书标签页
    ----booktag.xlsx　提取的图书标签页
	
----tool  抓取工具
```

# How to use?
1. Install python3.4 or another python3 version
2. Just install some python library if run was wrong
3. run step1.py
4. run step2.py
5. and so on

#如何使用
##step1.py：数据库初始化
```
python step1.py
```

step1.py代码：

```
# -*- coding:utf-8 -*-
import tool.mysql
# 新建数据库
result = tool.mysql.initdoubanbook()
print(result)
```

需先更改tool/mysql.py数据库用户名和密码

```
def init():
  return Mysql(host="localhost", user="root", pwd="passwd", db="doubanbook")

def initdoubanbook():
  mysql = pymysql.connect(host="localhost", user="root", passwd="passwd", charset="utf8")
```

<img src='https://raw.githubusercontent.com/hunterhug/doubanbook30000/master/img/step1.jpg' />
<img src='https://raw.githubusercontent.com/hunterhug/doubanbook30000/master/img/step11.jpg' />

##step2.py抓取页面进行测试
```
python step2.py
```

step2.py代码：

```
# -*- coding:utf-8 -*-
from tool.gethtml import getHtml
import bookdeal
# 抓取分类标签页
tag =getHtml('http://book.douban.com/tag/')
file = open('web/booktag.html','wb')
file.write(tag.encode())
file.close()

# 抓取列表页方便测试
tag1 = getHtml("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/book")
file1 = open('web/books.html','wb')
file1.write(tag1.encode())
file1.close()

# 抓取图书页方便测试
tag3 = getHtml("http://book.douban.com/subject/25862578/?from=tag_all")
file2 = open('web/book.html','wb')
file2.write(tag3.encode())
file2.close()
print("成功")
```
测试请直接运行bookdeal.py

##step3：抽取分类标签页存入Excel方便匹配分类
```
python step3.py
```

step3.py代码：

```
# -*- coding:utf-8 -*-
import bookdeal
# 提取标签页到excel
bookdeal.testbooktag()
```

<img src='https://raw.githubusercontent.com/hunterhug/doubanbook30000/master/img/step3.jpg' />

##step4.py抓取图书列表页
```
python step4.py
```

step4.py代码：

```
# -*- coding:utf-8 -*-
import catch
# 抓取各标签列表页
"""
  输入参数为:
  requireip 是否使用代理，默认否,代理文件在tool文件夹下daili.txt：http://www.youdaili.net/
  v 是否限制爬虫速度，默认否，时间为1秒仿人工
  lockprefix 文件加锁后缀
"""
catch.catchbooklist(0,2,'html')

```

<img src='https://raw.githubusercontent.com/hunterhug/doubanbook30000/master/img/step4.jpg' />


##step5.py提取图书列表页到Excel
```
python step5.py
```

step5.py代码：

```
# -*- coding:utf-8 -*-
import catch
# 提取各标签列表页到excel
catch.dealbooklist()
```


author:hunterhug